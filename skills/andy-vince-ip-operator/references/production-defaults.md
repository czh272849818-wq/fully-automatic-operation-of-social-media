# 内容生产默认值

## 配音

- 默认使用已确认的 ElevenLabs 音色 `Xinghe Jiang - Magnetic Conversational`，模型为 `Eleven Multilingual v2`。
- 默认参数：中文语速 1.2、英文语速 1.08、stability 0.35、similarity 0.82、style exaggeration 0.18，并启用 speaker boost。
- 本地 Vince 音色只是备用路径；只有用户明确说“用我自己的配音”时才启用，不得把它当作默认配音。

## BGM

- 项目默认签名 BGM 为已核验的 `Abstract Epic Technology Electronica_Star`（ComaStudio，Pixabay），沿用上一版已确认的视频方案：全程贯穿、低于口播、自动闪避，平台端不叠加第二首音乐。
- 如果在平台端选择新曲，必须核对曲名、作者和可用性，并遵守平台手册中的英文、史诗、有冲击力、不重复旧曲规则。

## 打包边界

- Skill 包不携带本地音频、参考音色、视频、图片、账号数据、日志、缓存或凭据。
- 生成内容时使用当前环境可访问的已授权素材；素材不可访问时标记缺口，不用猜测或冒充。
