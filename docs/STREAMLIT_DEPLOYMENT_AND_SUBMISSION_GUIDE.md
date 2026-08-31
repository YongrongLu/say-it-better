# 嘴替工作室：Streamlit 部署、录像与提交操作手册

## 1. 课程口径

本手册以课程 STAFF 的两条答复为准：

1. `cli_demo.py` 是在本地终端独立运行的纯文本 API 演示，不用它启动
   Streamlit。
2. Hugging Face 已取消 Spaces 中的免费原生 Streamlit SDK；本次作业
   改用 **Streamlit Community Cloud**，无需切回 Hugging Face。
3. 本项目是老师批准的**个人项目**。不需展示组员分工，但保留你自己的
   commit 和 pull request 记录作为可见贡献证据最稳妥。

GitHub 项目：<https://github.com/YongrongLu/say-it-better>

## 2. 哪里输入什么

- 标注 **VS Code 终端** 的命令：在 VS Code 顶部菜单选择
  **Terminal > New Terminal** 后输入。
- 标注 **VS Code 文件** 的内容：在左侧 Explorer 点开指定文件后编辑并保存。
- 标注 **浏览器** 的步骤：在 Chrome 中完成。
- 命令中的美元符号 `$` 只表示终端提示符，不要输入。

## 3. 部署前的安全检查

### 3.1 确认真实 token 只在 `.env`

**VS Code 文件：`.env`**

```dotenv
LITELLM_TOKEN=在这里放你的真实_Duke_Gateway_token
LITELLM_MODEL=gpt-5.6-sol
```

**VS Code 文件：`.env.example`**

```dotenv
LITELLM_TOKEN=replace_with_your_duke_gateway_token
LITELLM_MODEL=gpt-5.6-sol
```

`.env.example` 只能有占位符；不能放真实 token。两个文件都要按
`Command + S` 保存，但 `.env` 永远不 commit。

### 3.2 确认 Git 忽略 `.env`

**VS Code 终端：**

```bash
cd '/Users/ritaaa/Desktop/桌面 - Ritaaa的MacBook Air/Study/aipi/python_bootcamp/say-it-better'
git check-ignore -v .env
```

应该看到 `.gitignore` 中的 `.env` 规则。

再检查已追踪文件中是否有像真实 token 的内容：

```bash
git grep -nE 'sk-[A-Za-z0-9_-]{20,}'
```

理想结果是**没有任何输出**。如果出现了你真实的 token，立即去 Duke AI
Dashboard 撤销它，再清理 Git 历史。不要把扫描结果贴到上传文档。

## 4. 本地最终检查

### 4.1 进入项目并激活虚拟环境

**VS Code 终端：**

```bash
cd '/Users/ritaaa/Desktop/桌面 - Ritaaa的MacBook Air/Study/aipi/python_bootcamp/say-it-better'
source .venv/bin/activate
which python
```

`which python` 的结果应以
`say-it-better/.venv/bin/python` 结尾。

### 4.2 运行测试

```bash
python -m pytest -q
```

只有在结果显示全部通过时才继续。

### 4.3 单独运行 CLI

```bash
python cli_demo.py
```

依次输入内容、风格序号、沟通对象序号和语言序号。CLI 展示三个纯文本
候选版本，完成后回到终端提示符。

菜单序号：

- 风格 `1–10`：愤怒、讽刺、阴阳怪气、礼貌、温和、直接、正式、学术汇报、简历、
  工作面试。
- 对象 `1–6`：通用、朋友、同事、上级、教授、招聘者或面试官。
- 语言 `1–2`：中文、英文。

### 4.4 本地运行 Streamlit

保留当前终端，再新建一个终端。

**VS Code 终端 2：**

```bash
cd '/Users/ritaaa/Desktop/桌面 - Ritaaa的MacBook Air/Study/aipi/python_bootcamp/say-it-better'
source .venv/bin/activate
python -m streamlit run app.py
```

浏览器应打开 <http://localhost:8501>。亲自完成至少一次中文输出和一次
英文输出，确认：

- 文本输入可用。
- 风格、对象、输出语言会改变结果。
- 每次生成三个候选版本。
- 结果卡片和格式化比较表正常显示。

停止本地服务时，回到终端 2 按 `Control + C`。

## 5. 推送部署版本到 GitHub

首先查看改动：

```bash
git status --short
git diff --check
```

不要盲目使用 `git add .`。只添加你确认要提交的文件，例如：

```bash
git add README.md cli_demo.py tests/test_cli_demo.py \
  docs/VIDEO_DEMO_SCRIPT.md \
  docs/STREAMLIT_DEPLOYMENT_AND_SUBMISSION_GUIDE.md
git commit -m "docs: prepare Streamlit deployment and demo"
git push origin main
```

如果 `git status --short` 中还有你暂时不想提交的文件，不要把它写进
`git add` 命令。

## 6. 部署到 Streamlit Community Cloud

Streamlit 官方流程参考：

- <https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy>
- <https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management>

### 6.1 创建应用

1. **浏览器：**打开 <https://share.streamlit.io> 并用 GitHub 账号登录。
2. 授权 Streamlit 访问 `YongrongLu/say-it-better`。如果列表中看不到，在 GitHub
   授权设置中增加该仓库。
3. 左上角选择与仓库 owner 匹配的 workspace。这个项目的 owner 是
   `YongrongLu`。如果课程提供了 group/workspace，只有在仓库也归该组织所有
   时才选它。
4. 右上角点击 **Create app**。
5. 出现 **Do you already have an app?** 时选择 **Yup, I have an app**。
6. 填写：
   - Repository: `YongrongLu/say-it-better`
   - Branch: `main`
   - Main file path: `app.py`
   - App URL: 可尝试 `say-it-better-duke`；如被占用，换成系统建议名称。

### 6.2 设置 Python 和 Secrets

1. 点击 **Advanced settings**。
2. Python version 选择 **3.12**（Streamlit Community Cloud 当前默认版本）。
3. 在 **Secrets** 输入框粘贴下面的 TOML，并把占位符换成真实 token：

```toml
LITELLM_TOKEN = "PASTE_YOUR_REAL_DUKE_GATEWAY_TOKEN_HERE"
LITELLM_MODEL = "gpt-5.6-sol"
```

4. 点击 **Save**。
5. 回到部署表单，点击 **Deploy**。

这些是根层 secrets，Streamlit 会同时将它们暴露为环境变量，所以项目现有的
`os.getenv("LITELLM_TOKEN")` 不需要改成 `st.secrets`。

### 6.3 检查云端结果

1. 等待 build log 完成。
2. 打开分配的 `https://...streamlit.app` URL。
3. 用中英文各测试一次。
4. 用无痕窗口打开链接，确认老师不登录也能访问。
5. 如果不公开，在 app 的 **Settings > Sharing** 中设为 public。

如果出错：

- `LITELLM_TOKEN is missing`：进入 app 的 **Settings > Secrets**，检查名称和
  TOML 引号。
- `ModuleNotFoundError`：确认 `requirements.txt` 在仓库根目录并已 push。
- `Unauthorized`：重新创建 Duke token，只更新 Streamlit Secrets，不要提交到 Git。
- 修改代码后页面未更新：确认已 push 到 `main`，然后查看 Cloud logs 或
  reboot app。

## 7. 把 Live App 链接写回 README

**VS Code 文件：`README.md`**

将 Live App 下面的占位文本替换为真实链接：

```markdown
- [Live Streamlit app](https://你的子域名.streamlit.app)
```

保存后，在 **VS Code 终端**输入：

```bash
git add README.md
git commit -m "docs: add live Streamlit app link"
git push origin main
```

Community Cloud 以 GitHub 为源；push 后会自动更新应用。

## 8. 录制 60–120 秒视频

逐字稿见 [`VIDEO_DEMO_SCRIPT.md`](VIDEO_DEMO_SCRIPT.md)。录制顺序固定为：

1. GitHub 项目和简短介绍。
2. 终端运行 `python cli_demo.py`。
3. 本地 `http://localhost:8501` 的 Streamlit。
4. 线上 `https://...streamlit.app` 的 Streamlit。

这与 STAFF 说的 “CLI run → Streamlit locally → live app” 完全一致。

## 9. Canvas 四个提交框怎么填

如果 Canvas 题干还保留旧的 Hugging Face 文字，使用 STAFF 的最新口径，并在答案
中写清替代关系。

### 第 1 框：GitHub repository link

```text
https://github.com/YongrongLu/say-it-better
```

### 第 2 框：如果仍显示 Hugging Face Spaces repository link

填写 GitHub 源仓库，并附说明：

```text
Source repository for the Streamlit Community Cloud deployment:
https://github.com/YongrongLu/say-it-better

Per the course staff's updated guidance, this project uses Streamlit Community
Cloud instead of Hugging Face Spaces.
```

### 第 3 框：Live app link

```text
https://你的子域名.streamlit.app
```

### 第 4 框：Demo video

粘贴可公开访问的 60–120 秒视频链接，或使用 Canvas 的 **Insert Video** /
**Insert File** 上传。提交前用无痕窗口打开视频链接。

## 10. 个人项目的 GitHub 贡献说明

你不需要伪造组员或多人贡献。提交时可在备注中写：

```text
This is an instructor-approved individual project because I joined the course
after teams had been formed. All implementation, testing, documentation, and
deployment contributions are therefore under my own GitHub account.
```

你的 Git 历史已经包含可见 commit 和 merged pull request。无需为了模仿小组仓库再
创建虚假账号或无意义 PR。

## 11. 提交前最终清单

- [ ] GitHub 仓库是 public。
- [ ] README 包含本地运行、CLI 运行、Python 版本、截图和 live app 链接。
- [ ] `requirements.txt` 在仓库根目录。
- [ ] `python -m pytest -q` 全部通过。
- [ ] `python cli_demo.py` 可以独立运行并输出三个版本。
- [ ] 本地 Streamlit 可正常调用 API。
- [ ] 无痕窗口可访问 live Streamlit app。
- [ ] 云端 Secrets 含 `LITELLM_TOKEN` 和 `LITELLM_MODEL`。
- [ ] 真实 token 没有出现在源码、README、`.env.example` 或 Git 历史中。
- [ ] 视频在 60–120 秒之间，且按 CLI → local Streamlit → live app 的顺序展示。
- [ ] 视频链接不需要老师登录。
- [ ] Canvas 四个答案框都已填写。
- [ ] 备注说明这是老师批准的个人项目。
