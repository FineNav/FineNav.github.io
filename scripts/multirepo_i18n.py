"""Make multirepo's external files visible to static-i18n during a build.

multirepo 0.8.3 appends files outside docs_dir. static-i18n 1.3.1 skips such
Markdown files. Materialize imports inside docs_dir before i18n runs, retain
them through its recursive language builds, then remove only generated files.
"""
from pathlib import Path
import shutil

from mkdocs.plugins import event_priority
from mkdocs.structure.files import File

_generated = set()
_docs_root = None

def clean_generated():
    global _docs_root
    if _docs_root is None:
        return
    parents = set()
    for target in _generated:
        target.relative_to(_docs_root)
        target.unlink(missing_ok=True)
        parent = target.parent
        while parent != _docs_root:
            parents.add(parent)
            parent = parent.parent
    for parent in sorted(parents, key=lambda p: len(p.parts), reverse=True):
        try:
            parent.rmdir()
        except OSError:
            pass
    _generated.clear()
    _docs_root = None

@event_priority(-50)
def on_files(files, config):
    global _docs_root
    root = Path(config.docs_dir).resolve()
    _docs_root = root
    for file in list(files):
        if not hasattr(file, 'repo'):
            continue
        source = Path(file.abs_src_path).resolve()
        if source.is_relative_to(root):
            continue
        target = (root / file.src_uri).resolve()
        target.relative_to(root)
        if target.exists() and target not in _generated:
            raise ValueError(f'Imported document would overwrite a maintained file: {file.src_uri}')
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        _generated.add(target)
        replacement = File(file.src_uri, str(root), config.site_dir, config.use_directory_urls)
        replacement.repo = file.repo
        files.remove(file)
        files.append(replacement)
    return files

@event_priority(-200)
def on_post_build(config):
    # i18n's priority -100 post-build event completes all languages first.
    clean_generated()

def on_build_error(error):
    clean_generated()
