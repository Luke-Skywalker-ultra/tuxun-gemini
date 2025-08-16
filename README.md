AI模型Gemini分析图寻助手
这是一个利用Google Gemini AI来辅助进行“图寻”tuxun.fun游戏的python脚本。它通过游戏ID来自动获取当前题目的街景图片，并调用AI进行分析最可能的地理位置。省去了手动截图搜索的麻烦，用于学习AI接口以及图寻练习。

主要功能

全自动流程: 只需输入从浏览器地址栏复制的游戏ID，即可自动完成图片获取和分析。
AI强力分析: 集成 Google `gemini-2.5-pro` 模型，提供详细、带上下文的地理位置猜测。
结构化输出: AI返回格式化的地理位置信息，包括大洲、国家、省份/州、城市及其在上一级行政区划中的大致方位。
安全凭证管理: 使用 `.env` 文件安全地管理你的个人 API 密钥和 Cookie，避免敏感信息硬编码在代码中。
登录状态验证: 程序启动时会自动验证Tuxun Cookie的有效性，提前发现问题。


环境要求
* Python 3.9+
* 一个有效的 Google Gemini API 密钥
* 一个有效的图寻 (tuxun.fun) 账号 `fun_ticket` Cookie

## 安装与配置

请按照以下步骤来设置和运行本项目。

### 1. 下载项目

将本项目的所有文件（`main.py`, `tuxun_agent.py`等）下载到你本地的同一个文件夹中。

### 2. 安装依赖库


打开你的终端（Terminal），进入项目所在的文件夹，然后运行下面的命令来安装所有必需的 Python 库：

```bash
pip install -r requirements.txt

```

### 3. 创建并配置 `.env` 文件

这是最关键也最容易出错的步骤，用于存放你的个人凭证。

a. 在项目根目录下，创建一个名为 `.env` 的新文件。

b. 打开 `.env` 文件，并按照以下格式填入你的信息：

```
API_KEY="AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXX"
TUXUN_COOKIE="fun_ticket=eyJf...X0"

```

* **`API_KEY`**: 替换成你自己的 Google Gemini API 密钥。你可以从 [Google AI Studio](https://aistudio.google.com/app/apikey) 获取。
* **`TUXUN_COOKIE`**: 替换成你自己的图寻网站的 `fun_ticket`。**请仔细按照以下步骤操作**：
    1.  在浏览器中登录 [tuxun.fun](https://tuxun.fun)。
    2.  按 `F12` 打开开发者工具，切换到“网络(Network)”标签页。
    3.  刷新页面或开始一局新游戏，在请求列表中找到任意一个发往 `tuxun.fun` 的请求。
    4.  在右侧的“请求标头(Request Headers)”中找到 `Cookie:` 这一行。
    5.  在 `Cookie:` 的完整字符串中，找到以 `fun_ticket=` 开头的部分。
    6.  **只复制 `fun_ticket=...` 这一段**（直到下一个分号 `;` 前或字符串末尾），并将其粘贴到 `.env` 文件中。



## 如何使用

1.  确保你的 `.env` 文件已经正确配置。
2.  在终端中，进入项目文件夹。
3.  运行主程序：
    ```bash
    python main.py
    ```
4.  程序启动并验证Cookie成功后，会提示你输入游戏ID。
5.  从图寻游戏页面的浏览器地址栏复制游戏ID（例如 `Ge9g36p53Vf2yAL9`），粘贴到终端里并按回车。
6.  等待几秒钟，AI的分析结果就会显示出来。
7.  你可以持续输入新的游戏ID进行分析。如果想退出程序，输入 `q` 并按回车。



## 注意事项

* 请妥善保管你的 `.env` 文件，不要将它分享给他人或上传到公共代码仓库（`.gitignore` 文件已配置忽略它）。
* 本项目调用 Google Gemini API，请遵守 Google 的服务条款。免费额度对于个人使用完全足够，详情请参考官方定价页面。
* 本项目仅供学习和技术交流使用。详细交流优化更新+q：3487333091（备注来意）








