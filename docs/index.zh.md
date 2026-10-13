# FineNav 开发者文档

FineNav 提供构建机器人导航应用的工具与组件。
通过 FineNav-Engine，在 ROS 2 C++ 应用中装配 Map、Planner 和 WorldView。

## 从 FineNav-Engine 开始

1. 阅读 [Engine 项目总览](finenav-engine/index.md)，了解组件职责。
2. 按照[快速开始](finenav-engine/guide/quickstart.md)下载源码、安装依赖、
   编译工作空间并运行示例。
3. [选择 Map 和 Planner](finenav-engine/guide/choose-algorithms.md)，
   [编写 WorldView](finenav-engine/guide/worldview.md)，
   然后[配置应用](finenav-engine/guide/cpp-application.md)。

## 组件与扩展

通过[插件目录](finenav-engine/guide/plugins/index.md)查阅当前组件信息。
需要开发自己的算法时，阅读[自定义 Planner](finenav-engine/guide/custom-planner.md)
和[自定义 Map](finenav-engine/guide/custom-map.md)。

`finenav_map` 和 `finenav_planner` 仓库提供文档源后，将接入各自的模块说明。

英文是默认语言，可通过语言切换器查看中文；尚未翻译的页面显示英文内容。
部分源码链接需要对应的 GitHub 仓库访问权限。
