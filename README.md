## 总体设计

### 决策

基于图片、问题和预设的指令集合，CLIP模型根据图片和问题匹配出最合适的指令

### 执行

根据指令控制机械臂的动作

> 图中有苹果、手枪和4个垃圾桶。query: Throw the fruit away。CLIP将query匹配到指令如throw apple away，YOLO模型定位apple，控制机械臂扔进绿色垃圾桶

## Milestone

- [x] CLIP问题与答案匹配

- [ ] 构造预设的指令集

- [x] YOLO定位物体

- [ ] 指令集到动作的映射

- [ ] 机械臂控制