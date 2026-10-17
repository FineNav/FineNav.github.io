# FineNav 开发者文档

FineNav 提供用于构建机器人导航应用的工具与组件。

## FineNav-Engine

选择 Map 和 Planner，通过 WorldView 对接地图查询，
在 C++ 中组装控制 pipeline，再通过行为树配置任务执行方式。

- [项目总览](finenav-engine/index.md)
- [如何安装](finenav-engine/guide/installation.md)：环境配置、下载源码与编译。
- 基于 `finenav_example` 的入门教程：
    1. [运行示例，查看效果](finenav-engine/guide/quickstart.md)
    2. [选择 Map 和 Planner](finenav-engine/guide/choose-algorithms.md)
    3. [编写 WorldView](finenav-engine/guide/worldview.md)
    4. [组装控制 Pipeline](finenav-engine/guide/cpp-application.md)
    5. [按需求配置行为树](finenav-engine/guide/behavior-tree.md)
- [finenav_planners](finenav-engine/guide/plugins/planners.md)
- [finenav_maps](finenav-engine/guide/plugins/maps.md)

## FineNav-SlamBox

[文档占位](slambox.md)，后续补充该仓库的专属使用说明。

## FineNav（ICRA 版本）

[文档占位](icra.md)，后续补充该仓库的专属使用说明。

可通过语言切换器查看中英文版本。部分源码链接需要对应的 GitHub 仓库访问权限。
