# CyberHR 增量 Merge 逻辑

当用户追加新的面试记录、评语、制度文件或沟通材料时，把增量信息合并进现有的 `hr_memory.md`、`hr_persona.md` 与 `team.json`。

原则：
1. 新证据优先追加，不粗暴覆盖旧结论
2. 若新旧冲突，标注冲突并保留上下文
3. 事实更新进 HR Memory，风格更新进 HR Persona，角色分工更新进 Team
4. 强化结论时必须说明依据来自哪些新材料
