<div align="center">

# 数学三部曲

### 高等数学 · 线性代数 · 概率论与数理统计

面向大学期末复习、考研备考与数学爱好者的中文 LaTeX 数学讲义，共 529 页。

[![LaTeX](https://img.shields.io/badge/LaTeX-XeLaTeX-008080?logo=latex&logoColor=white)](https://www.latex-project.org/)
[![License](https://img.shields.io/badge/License-CC_BY--NC_4.0-EF9421?logo=creativecommons&logoColor=white)](LICENSE)
[![Release](https://img.shields.io/github/v/release/YOUR_GITHUB_USERNAME/math-review-notes?color=blue)](https://github.com/YOUR_GITHUB_USERNAME/math-review-notes/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/YOUR_GITHUB_USERNAME/math-review-notes/total?color=brightgreen)](https://github.com/YOUR_GITHUB_USERNAME/math-review-notes/releases)
[![Stars](https://img.shields.io/github/stars/YOUR_GITHUB_USERNAME/math-review-notes?style=flat&color=yellow)](https://github.com/YOUR_GITHUB_USERNAME/math-review-notes/stargazers)

[下载最新版 PDF](https://github.com/YOUR_GITHUB_USERNAME/math-review-notes/releases/latest)
·
[查看源码](#项目结构)
·
[自行编译](#自行编译)

</div>

---

## 项目简介

本项目收录三册中文数学复习讲义：

- 《高等数学考研与竞赛复习册》
- 《线性代数考研与竞赛复习册》
- 《概率论与数理统计考研与竞赛复习册》

全书使用 LaTeX 编写，以定义、定理、方法、例题、习题和完整解答组成知识闭环，适合大学课程复习、考研数学备考以及系统查阅。

## 核心特色

- **完整知识体系**：三册共 27 章，覆盖大学数学的主要内容。
- **推导过程详细**：保留关键步骤、适用条件与方法依据。
- **数学审校完整**：公式、定理条件、例题数据和习题答案均经过系统核查。
- **排版清晰美观**：统一使用 XeLaTeX 排版，支持中文、公式、图表和 PDF 书签。
- **题型层次丰富**：包含基础题、考研题、提高题与竞赛拓展。
- **答案可直接查阅**：章末习题配有提示、推导和完整解答。
- **源码结构清晰**：三册可以独立编译，便于阅读、修改和二次整理。

## 内容概览

| 书册 | 主要内容 | 页数 | 源码目录 |
|---|---|---:|---|
| 高等数学 | 极限、微积分、微分方程、多元函数、重积分、曲线曲面积分、级数 | 286 | [`book/`](book/) |
| 线性代数 | 行列式、矩阵、向量组、方程组、特征值、二次型、线性空间 | 136 | [`book_linear/`](book_linear/) |
| 概率论与数理统计 | 概率、随机变量、数字特征、极限定理、参数估计、检验、回归 | 107 | [`book_probability/`](book_probability/) |

## 页面预览

<!-- 发布截图后取消下面三行注释，并将图片放入 docs/images/。 -->
<!-- ![高等数学页面预览](docs/images/calculus-preview.png) -->
<!-- ![线性代数页面预览](docs/images/linear-algebra-preview.png) -->
<!-- ![概率论页面预览](docs/images/probability-preview.png) -->

> 截图展示区：建议选取章节首页、公式密集页和完整例题页各一张。

## 三册目录

<details>
<summary><strong>《高等数学考研与竞赛复习册》</strong></summary>

1. 函数、极限与连续
2. 一元函数微分学
3. 一元函数积分学
4. 常微分方程
5. 向量代数与空间解析几何
6. 多元函数微分学
7. 重积分
8. 曲线积分、曲面积分与场论初步
9. 无穷级数与函数展开
10. 附录：公式速查、习题解答、方法导航与索引

</details>

<details>
<summary><strong>《线性代数考研与竞赛复习册》</strong></summary>

1. 行列式：从展开到结构
2. 矩阵：运算、求逆与秩
3. 向量组：相关性、基与坐标
4. 线性方程组：解的存在与结构
5. 特征值与相似：寻找合适的基
6. 二次型：合同、惯性与正定
7. 线性空间与线性变换
8. 提高专题：秩、多项式与矩阵分解
9. 附录：公式速查、习题解答与概念索引

</details>

<details>
<summary><strong>《概率论与数理统计考研与竞赛复习册》</strong></summary>

1. 随机事件与概率
2. 随机变量及其分布
3. 多维随机变量及其分布
4. 随机变量的数字特征
5. 大数定律与中心极限定理
6. 数理统计的基本概念与抽样分布
7. 参数估计
8. 假设检验
9. 方差分析与一元线性回归
10. 测度论选学：概率的积分视角
11. 附录：公式速查、习题详解与题型索引

</details>

## 项目结构

```text
math-review-notes/
├── book/                         # 高等数学
│   ├── main.tex
│   ├── preamble.tex
│   ├── frontmatter/
│   ├── chapters/
│   ├── appendix/
│   └── assets/
├── book_linear/                  # 线性代数
│   ├── main.tex
│   ├── preamble.tex
│   ├── frontmatter/
│   ├── chapters/
│   ├── derivations/
│   ├── enrichment/
│   ├── appendix/
│   └── assets/
├── book_probability/             # 概率论与数理统计
│   ├── main.tex
│   ├── preamble.tex
│   ├── frontmatter/
│   ├── chapters/
│   ├── appendix/
│   ├── bib/
│   └── assets/
├── README.md
├── LICENSE
└── .gitignore
```

## 下载 PDF

推荐从 [GitHub Releases](https://github.com/YOUR_GITHUB_USERNAME/math-review-notes/releases/latest) 下载已经编译完成的版本：

- `高等数学考研与竞赛复习册.pdf`
- `线性代数考研与竞赛复习册.pdf`
- `概率论与数理统计考研与竞赛复习册.pdf`

PDF 文件作为每个版本的 Release Assets 发布，不写入 Git 历史。

## 自行编译

请先安装完整的 [TeX Live](https://www.tug.org/texlive/) 或 [MiKTeX](https://miktex.org/) 环境，并确保 `xelatex` 与 `latexmk` 可用。

进入任一书册目录后执行：

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

例如编译高等数学：

```bash
cd book
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

清理编译辅助文件：

```bash
latexmk -c
```

编译生成的 PDF 位于相应目录的 `main.pdf`。

## 反馈与贡献

如发现笔误、公式问题、交叉引用错误或排版异常，欢迎提交 [Issue](https://github.com/YOUR_GITHUB_USERNAME/math-review-notes/issues) 或 [Pull Request](https://github.com/YOUR_GITHUB_USERNAME/math-review-notes/pulls)。

提交问题时请尽量注明所属书册、章节与页码，并附上原文、截图或建议修改方式。

## 致谢

感谢 LaTeX、CTeX、TikZ 及相关开源宏包的维护者。封面图片、字体及其他第三方素材分别遵循其原始授权协议，相关署名信息保留在书册或素材目录中。

## 开源许可

除特别注明的第三方素材外，本项目的讲义正文、LaTeX 排版内容与 PDF 采用 [CC BY-NC 4.0](LICENSE) 许可；独立程序和自动化脚本采用 MIT License。

你可以在保留署名、注明修改并遵守非商业使用要求的前提下分享和改编讲义内容。如需商业使用，请提前联系作者取得单独授权。

---

<div align="center">

如果这些笔记对你有帮助，欢迎点亮一个 ⭐

Copyright © 2026 雪落长安无声

</div>
