---
layout: post
author: Yosef Pogrow
title:  "testing the system (not real post)"
date:   2017-03-15 14:02:35 +0200
categories: sublinear algorithm
comments: true
---

<div id="globalWrapper">
<script type="math/tex">
\newcommand{\lyxlock}{}
</script>
<noscript>
<div class="warning">
Warning: <a href="http://www.mathjax.org/">MathJax</a> requires JavaScript to correctly process the mathematics on this page. Please enable JavaScript on your browser.
</div><hr/>
</noscript>
<h1 class="title">
Sublinear Algorithms - Summary
</h1>
<h2 class="author">
Eran Amar
</h2>
<h1 class="Section">
<a class="toc" name="toc-Section-1">1</a> Tricks
</h1>
<div class="Description">
<span class="Description-entry">Variance-Reduction:</span> When have a R.V. <span class="MathJax_Preview"><script type="math/tex">
X
</script>
</span> with expectation <span class="MathJax_Preview"><script type="math/tex">
\mu
</script>
</span> and <span class="MathJax_Preview"><script type="math/tex">
V\left(X\right)=\mathcal{O}\left(\mu^{2}\right)
</script>
</span> can’t use Chebyshev because the standard deviation is too large. Thus repeating the estimation <span class="MathJax_Preview"><script type="math/tex">
k:=\mathcal{O}\left(1/\epsilon^{2}\right)
</script>
</span> independent times and returning the average estimations <span class="MathJax_Preview"><script type="math/tex">
\bar{X}:=\sum_{j=1}^{k}\frac{X_{j}}{k}
</script>
</span>. In that way <span class="MathJax_Preview"><script type="math/tex">
\mathbb{E}\left[\bar{X}\right]=\mu
</script>
</span> but <span class="MathJax_Preview"><script type="math/tex">
V\left(\bar{X}\right)=\frac{1}{k}V\left(X\right)=\epsilon^{2}V\left(X\right)\implies\sigma=\epsilon\mu
</script>
</span>. Then apply Chebushev’s inequality to get constant high probability for <span class="MathJax_Preview"><script type="math/tex">
\bar{X}\in\left(1\pm\epsilon\right)\mu
</script>
</span>.
</div>
<div class="Description">
<span class="Description-entry">Exponential-Concentration:</span> Given a trial <span class="MathJax_Preview"><script type="math/tex">
X
</script>
</span> with high constant success probability <span class="MathJax_Preview"><script type="math/tex">
p>\frac{1}{2}
</script>
</span> and we want to boost its success probability up to <span class="MathJax_Preview"><script type="math/tex">
1-\delta
</script>
</span>. The goal is to use Chernoff\Hoeffding bounds by running <span class="MathJax_Preview"><script type="math/tex">
t:=c\cdot\log\frac{1}{\delta}
</script>
</span> (for some constant that will be determined later) independent copies of the algorithm <span class="MathJax_Preview"><script type="math/tex">
\left\{ X_{i}\right\} _{i=1}^{t}
</script>
</span>, then returning the median/majority <span class="MathJax_Preview"><script type="math/tex">
Y
</script>
</span>. Hence <span class="MathJax_Preview">
<script type="math/tex;mode=display">

\mathbf{P}\left[Y\mbox{ is wrong}\right]\le\mathbf{P}\left[\sum_{i}X_{i}<\frac{t}{2}\right]=\mathbf{P}\left[\sum_{i}X_{i}<\left(1-\epsilon\right)\mu\right]

</script>

</span>
 where <span class="MathJax_Preview"><script type="math/tex">
\mu:=pt
</script>
</span> and <span class="MathJax_Preview"><script type="math/tex">
\epsilon:=1-\frac{1}{2p}
</script>
</span>, so <span class="MathJax_Preview"><script type="math/tex">
\mathbf{P}\left[\sum_{i}X_{i}<\left(1-\epsilon\right)\mu\right]\le\exp\left(-\epsilon^{2}\mu/2\right)=\exp\left(\frac{-\left(1-1/2p\right)^{2}p\left(c\log\frac{1}{\delta}\right)}{2}\right)=\delta
</script>
</span> for appropriate choice of <span class="MathJax_Preview"><script type="math/tex">
c
</script>
</span>.
</div>
<h1 class="Section">
<a class="toc" name="toc-Section-2">2</a> Basic Streaming Models
</h1>
<h2 class="Subsection">
<a class="toc" name="toc-Subsection-2.1">2.1</a> Probabilistic Counting
</h2>
<h3 class="Subsubsection-">
<a class="toc" name="toc-Subsubsection--1"></a>Problem Definition
</h3>
<div class="Unindented">
Estimate the length of the given stream.
</div>
<h3 class="Subsubsection-">
<a class="toc" name="toc-Subsubsection--2"></a>Algorithms
</h3>
<ol>
<li>
Morris: maintain a counter <span class="MathJax_Preview"><script type="math/tex">
X=0
</script>
</span>, at each element, increment it w.p. <span class="MathJax_Preview"><script type="math/tex">
2^{-X}
</script>
</span>. Output <span class="MathJax_Preview"><script type="math/tex">
2^{X}-1
</script>
</span>.\begin_inset Separator latexpar\end_inset<ol>
<li>
<span class="MathJax_Preview"><script type="math/tex">
\mathbb{E}\left(2^{X}-1\right)=m
</script>
</span>, <span class="MathJax_Preview"><script type="math/tex">
V\left(2^{X}-1\right)\le\frac{3m\left(m+1\right)}{2}+1=\mathcal{O}\left(\mathbb{E}^{2}\left(2^{X}\right)\right)
</script>
</span>.
</li>

</ol>

</li>
<li>
Morris+: run <span class="MathJax_Preview"><script type="math/tex">
k:=\mathcal{O}\left(1/\epsilon^{2}\right)
</script>
</span> independent copies of Morris and output the average. [variance reduction trick]
</li>

</ol>
<h2 class="Subsection">
<a class="toc" name="toc-Subsection-2.2">2.2</a> Revisior Sampling
</h2>
<div class="Description">
<span class="Description-entry">Problem-Definition:</span> Pick uniformly at random an element from the stream.
</div>
<div class="Description">
<span class="Description-entry">Algorithm:</span> maintain a running index <span class="MathJax_Preview"><script type="math/tex">
j
</script>
</span> and a candidate <span class="MathJax_Preview"><script type="math/tex">
s
</script>
</span>. For each <span class="MathJax_Preview"><script type="math/tex">
j
</script>
</span> update <span class="MathJax_Preview"><script type="math/tex">
s=\sigma_{j}
</script>
</span> w.p. <span class="MathJax_Preview"><script type="math/tex">
1/j
</script>
</span>.
</div>
<h1 class="Section">
<a class="toc" name="toc-Section-3">3</a> Frequency Vectors
</h1>
<div class="Unindented">
In those problems, the stream is <span class="MathJax_Preview"><script type="math/tex">
\left(\sigma_{1},..,\sigma_{m}\right)\in\left[n\right]^{m}
</script>
</span> and there is a frequency vector <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}\in\mathbb{Z}^{n}
</script>
</span> s.t. <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}_{i}=\#\mbox{ of appeareances of \ensuremath{i\in\left[n\right]} in the stream}.
</script>
</span> The frequency vector is implicit and not given nor stored in the algorithm. 
</div>
<h2 class="Subsection">
<a class="toc" name="toc-Subsection-3.1">3.1</a> Distinct Elements
</h2>
<h3 class="Subsubsection-">
<a class="toc" name="toc-Subsubsection--3"></a>Problem Definition
</h3>
<div class="Unindented">
Estimate <span class="MathJax_Preview"><script type="math/tex">
\left|\left|\mathbf{x}\right|\right|_{0}:=\left|\left\{ i:\:\mathbf{x}_{i}>0\right\} \right|
</script>
</span> i.e. the number of different elements in the stream (denoted as <span class="MathJax_Preview"><script type="math/tex">
d^{*}
</script>
</span>).
</div>
<h3 class="Subsubsection-">
<a class="toc" name="toc-Subsubsection--4"></a>Algorithms
</h3>
<ol>
<li>
FM: Use hash <span class="MathJax_Preview"><script type="math/tex">
h:\left[n\right]\mapsto\left[0,1\right]
</script>
</span> and keep <span class="MathJax_Preview"><script type="math/tex">
Z=\min\left\{ Z,\:h\left(\sigma_{j}\right)\right\} 
</script>
</span> running over <span class="MathJax_Preview"><script type="math/tex">
j
</script>
</span>. \begin_inset Separator latexpar\end_inset<ol>
<li>
<span class="MathJax_Preview"><script type="math/tex">
\mathbb{E}\left(Z\right)=1/\left(d^{*}+1\right)
</script>
</span>, <span class="MathJax_Preview"><script type="math/tex">
V\left(Z\right)\le\mathbb{E}^{2}\left[Z\right]=\frac{2}{\left(d^{*}+1\right)\left(d^{*}+2\right)}=\mathcal{O}\left(\mathbb{E}^{2}\left(Z\right)\right)
</script>
</span>.
</li>

</ol>

</li>
<li>
FM+: run <span class="MathJax_Preview"><script type="math/tex">
k:=\mathcal{O}\left(1/\epsilon^{2}\right)
</script>
</span> independent copies of FM (each has own hash) and output the average of the estimators. [variance reduction trick]
</li>
<li>
Bottom-k: Use hash <span class="MathJax_Preview"><script type="math/tex">
h:\left[n\right]\mapsto\left[0,1\right]
</script>
</span>. Keep <span class="MathJax_Preview"><script type="math/tex">
k
</script>
</span> minimum values <span class="MathJax_Preview"><script type="math/tex">
z_{1}\ge..\ge z_{k}
</script>
</span> from the set <span class="MathJax_Preview"><script type="math/tex">
\left\{ 1_{1},..,1_{k},h\left(\sigma_{1}\right),..,h\left(\sigma_{m}\right)\right\} 
</script>
</span>and output <span class="MathJax_Preview"><script type="math/tex">
k/z_{k}
</script>
</span>.\begin_inset Separator latexpar\end_inset<ol>
<li>
Compute directly <span class="MathJax_Preview"><script type="math/tex">
\mathbf{P}\left[\frac{k}{z_{k}}\in\left(1+\epsilon\right)d^{*}\right]\ge0.9
</script>
</span>.
</li>

</ol>

</li>

</ol>
<h2 class="Subsection">
<a class="toc" name="toc-Subsection-3.2">3.2</a> <span class="MathJax_Preview"><script type="math/tex">
\ell_{p}
</script>
</span> Point Query
</h2>
<h3 class="Subsubsection-">
<a class="toc" name="toc-Subsubsection--5"></a>Problem Definition
</h3>
<div class="Unindented">
Given <span class="MathJax_Preview"><script type="math/tex">
p,\alpha
</script>
</span> estimate <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}_{i}
</script>
</span> for any <span class="MathJax_Preview"><script type="math/tex">
i
</script>
</span> with error of <span class="MathJax_Preview"><script type="math/tex">
\pm\alpha\cdot\left|\left|\mathbf{x}\right|\right|_{p}
</script>
</span>. 
</div>
<h3 class="Subsubsection-">
<a class="toc" name="toc-Subsubsection--6"></a>Algorithms for <span class="MathJax_Preview"><script type="math/tex">
p=1
</script>
</span>
</h3>
<ol>
<li>
CountMin: Init <span class="MathJax_Preview"><script type="math/tex">
w:=\mathcal{O}\left(\alpha^{-1}\right)
</script>
</span> bucket <span class="MathJax_Preview"><script type="math/tex">
S=\left[s_{1},..,s_{w}\right]
</script>
</span> and use hash <span class="MathJax_Preview"><script type="math/tex">
h:\left[n\right]\mapsto\left[w\right]
</script>
</span> to map items to buckets: <span class="MathJax_Preview"><script type="math/tex">
s_{y}=\sum_{z:h\left(z\right)=y}\mathbf{x}_{z}
</script>
</span>. For any <span class="MathJax_Preview"><script type="math/tex">
i
</script>
</span> output <span class="MathJax_Preview"><script type="math/tex">
s_{h\left(i\right)}
</script>
</span>. 
</li>
<li>
CountMin+ (positive frequencies only): run <span class="MathJax_Preview"><script type="math/tex">
t:=\log n
</script>
</span> independent copies of CountMin (each has own hash) and output the <i>minimum</i> of the resulting estimators. [exponential concentration trick]
</li>
<li>
CountMin++ (general <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}
</script>
</span>): run <span class="MathJax_Preview"><script type="math/tex">
t:=\log n
</script>
</span> independent copies of CountMin (each has own hash) and output the <i>median</i> of the resulting estimators. [exponential concentration trick]
</li>

</ol>
<h3 class="Subsubsection-">
<a class="toc" name="toc-Subsubsection--7"></a>Algorithms for <span class="MathJax_Preview"><script type="math/tex">
p=2
</script>
</span>
</h3>
<ol>
<li>
CountSketch: Init <span class="MathJax_Preview"><script type="math/tex">
w:=\mathcal{O}\left(\alpha^{-1}\right)
</script>
</span> bucket <span class="MathJax_Preview"><script type="math/tex">
S=\left[s_{1},..,s_{w}\right]
</script>
</span> and fix independently uniformly at random <span class="MathJax_Preview"><script type="math/tex">
r_{1},..,r_{n}\in\left\{ \pm1\right\} 
</script>
</span>. Choose hash <span class="MathJax_Preview"><script type="math/tex">
h:\left[n\right]\mapsto\left[w\right]
</script>
</span> to map items to buckets: <span class="MathJax_Preview"><script type="math/tex">
s_{y}=\sum_{z:h\left(z\right)=y}r_{z}\cdot\mathbf{x}_{z}
</script>
</span>. For any <span class="MathJax_Preview"><script type="math/tex">
i
</script>
</span> output <span class="MathJax_Preview"><script type="math/tex">
r_{i}\cdot s_{h\left(i\right)}
</script>
</span>. 
</li>
<li>
CountSketch+ (not seen in class): run <span class="MathJax_Preview"><script type="math/tex">
t:=\log n
</script>
</span> independent copies of CountSketch (each has own randomness) and output the <i>median</i> of the resulting estimators. [exponential concentration trick]
</li>

</ol>
<h1 class="Section">
<a class="toc" name="toc-Section-4">4</a> Frequency Moments
</h1>
<h3 class="Subsubsection-">
<a class="toc" name="toc-Subsubsection--8"></a>Problem Definition
</h3>
<div class="Unindented">
Given <span class="MathJax_Preview"><script type="math/tex">
p,\epsilon
</script>
</span> estimate <span class="MathJax_Preview"><script type="math/tex">
\left|\left|\mathbf{x}\right|\right|_{p}^{p}
</script>
</span> within error of <span class="MathJax_Preview"><script type="math/tex">
\pm\epsilon\cdot\left|\left|\mathbf{x}\right|\right|_{p}
</script>
</span>. 
</div>
<h3 class="Subsubsection-">
<a class="toc" name="toc-Subsubsection--9"></a>Algorithms for <span class="MathJax_Preview"><script type="math/tex">
p=2
</script>
</span>
</h3>
<ol>
<li>
AMS (Tug-of-War): Fix independently uniformly at random <span class="MathJax_Preview"><script type="math/tex">
r_{1},..,r_{n}\in\left\{ \pm1\right\} 
</script>
</span>. Maintain <span class="MathJax_Preview"><script type="math/tex">
Z=\sum_{i=1}^{n}r_{i}\mathbf{x}_{i}
</script>
</span> (in streaming way: given <span class="MathJax_Preview"><script type="math/tex">
\sigma_{j}
</script>
</span> update <span class="MathJax_Preview"><script type="math/tex">
Z+=r_{j}
</script>
</span>) finally output <span class="MathJax_Preview"><script type="math/tex">
Z^{2}
</script>
</span>. Note that it is enough that <span class="MathJax_Preview"><script type="math/tex">
\left\{ r_{j}\right\} 
</script>
</span> are only 4-independent (instead of fully independent).\begin_inset Separator latexpar\end_inset<ol>
<li>
<span class="MathJax_Preview"><script type="math/tex">
\mathbb{E}\left[Z^{2}\right]=\left|\left|\mathbf{x}\right|\right|_{2}
</script>
</span>, <span class="MathJax_Preview"><script type="math/tex">
V\left(Z^{2}\right)\le3\left(\mathbb{E}\left[Z^{2}\right]\right)^{2}
</script>
</span> .
</li>

</ol>

</li>
<li>
AMS+: run <span class="MathJax_Preview"><script type="math/tex">
t:=\log n
</script>
</span> independent copies of AMS (each has own randomness) and output the average of the resulting estimators. [variance reduction trick] Remark - estimating <span class="MathJax_Preview"><script type="math/tex">
\left|\left|\mathbf{x}\right|\right|_{2}^{2}
</script>
</span> and not <span class="MathJax_Preview"><script type="math/tex">
\left|\left|\mathbf{x}\right|\right|_{2}
</script>
</span>.
</li>

</ol>
<h3 class="Subsubsection-">
<a class="toc" name="toc-Subsubsection--10"></a>Algorithms for <span class="MathJax_Preview"><script type="math/tex">
p\in\left(2,\infty\right)
</script>
</span>
</h3>
<ol>
<li>
PSL sketch (Precision Sampling Lemma): \begin_inset Separator latexpar\end_inset<ol>
<li>
Initialization: Let <span class="MathJax_Preview"><script type="math/tex">
w:=\mathcal{O}\left(\left(\log n\right)^{\mathcal{O}\left(1\right)}\cdot n^{1-\frac{2}{p}}\right)
</script>
</span> and choose random hash function <span class="MathJax_Preview"><script type="math/tex">
h:\left[n\right]\mapsto\left[w\right]
</script>
</span>. Pick i.i.d signs <span class="MathJax_Preview"><script type="math/tex">
r_{1},..,r_{n}\in\left\{ \pm1\right\} 
</script>
</span> and random precision <span class="MathJax_Preview"><script type="math/tex">
u_{1},..,u_{n}\sim Exp\left(1\right)
</script>
</span>.
</li>
<li>
Update: maintain vector <span class="MathJax_Preview"><script type="math/tex">
S:=\left[S_{1},..,S_{w}\right]
</script>
</span> where <span class="MathJax_Preview"><script type="math/tex">
S_{j}:=\sum_{i:h\left(i\right)=j}\frac{r_{i}x_{i}}{u_{i}^{1/p}}
</script>
</span>
</li>
<li>
Output: <span class="MathJax_Preview"><script type="math/tex">
\max_{j\in\left[w\right]}\left|S_{j}\right|^{p}
</script>
</span>
</li>

</ol>

</li>

</ol>
<div class="Unindented">
Storage <span class="MathJax_Preview"><script type="math/tex">
w\log n
</script>
</span> bits without randomness. 
</div>
<h2 class="Subsection">
<a class="toc" name="toc-Subsection-4.1">4.1</a> Heavy Hitters
</h2>
<div class="Unindented">
Given <span class="MathJax_Preview"><script type="math/tex">
p,\phi,\epsilon
</script>
</span> define <span class="MathJax_Preview"><script type="math/tex">
HH_{\phi}^{p}\left(\mathbf{x}\right):=\left\{ i\in\left[n\right]:\;\left|\mathbf{x}_{i}\right|\ge\phi\left|\left|\mathbf{x}\right|\right|_{p}\right\} 
</script>
</span>. Note that <span class="MathJax_Preview"><script type="math/tex">
\left|HH_{\phi}^{p}\left(\mathbf{x}\right)\right|\le\frac{1}{\phi^{p}}
</script>
</span> for any <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}
</script>
</span>. For any <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}
</script>
</span> want to return estimation <span class="MathJax_Preview"><script type="math/tex">
S\subset\left[n\right]
</script>
</span> s.t. <span class="MathJax_Preview"><script type="math/tex">
HH_{\phi}^{p}\left(\mathbf{x}\right)\subseteq S\subseteq HH_{\phi\left(1-\epsilon\right)}^{p}\left(\mathbf{x}\right)
</script>
</span>. Solved by reduction to suitable version of Point Query (according to <span class="MathJax_Preview"><script type="math/tex">
p
</script>
</span>).
</div>
<h2 class="Subsection">
<a class="toc" name="toc-Subsection-4.2">4.2</a> Compressed Sensing \ Sparse Recovery
</h2>
<div class="Unindented">
Given <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}\in\mathbb{R}^{n}
</script>
</span> and can observe only <span class="MathJax_Preview"><script type="math/tex">
y_{i}=\left\langle \mathbf{x},A_{i}\right\rangle 
</script>
</span> where <span class="MathJax_Preview"><script type="math/tex">
A_{1},..,A_{p}
</script>
</span> are vectors of our choice. Need to design the vectors <span class="MathJax_Preview"><script type="math/tex">
A_{j}
</script>
</span> to be able to recover <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}
</script>
</span> (we focus on the case where we choose all <span class="MathJax_Preview"><script type="math/tex">
\left\{ A_{j}\right\} 
</script>
</span> in advance). First we design an algorithm to sparse vectors (easier) than for approximately sparse. 
</div>
<div class="Indented">
For <span class="MathJax_Preview"><script type="math/tex">
k
</script>
</span>-sparse vectors (<span class="MathJax_Preview"><script type="math/tex">
\left|\left|\mathbf{x}\right|\right|_{0}=k
</script>
</span>), can use CountMin to estimate each coordinate with <span class="MathJax_Preview"><script type="math/tex">
p=\mathcal{O}\left(\alpha^{-1}\log n\right)
</script>
</span> vectors. If also <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}\in\left\{ 0,1\right\} ^{n}
</script>
</span> then with choice of <span class="MathJax_Preview"><script type="math/tex">
\alpha:=1/3k
</script>
</span> can distinguish between <span class="MathJax_Preview"><script type="math/tex">
0
</script>
</span> and <span class="MathJax_Preview"><script type="math/tex">
1
</script>
</span> on each coordinate, i.e. fully recover the source. Regarding <i>approximately</i> <span class="MathJax_Preview"><script type="math/tex">
k
</script>
</span>-sparse input: the best <span class="MathJax_Preview"><script type="math/tex">
k
</script>
</span>-sparse recovery has an unavoidable error of <span class="MathJax_Preview"><script type="math/tex">
\left|\left|\mathbf{x}_{tail\left(k\right)}\right|\right|
</script>
</span> where <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}_{tail\left(k\right)}
</script>
</span> is the same as <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}
</script>
</span> after replacing the heaviest <span class="MathJax_Preview"><script type="math/tex">
k
</script>
</span> coordinates with zeroes. We saw in class that with <span class="MathJax_Preview"><script type="math/tex">
\alpha:=\epsilon/k
</script>
</span> CountMin+ returns an estimator <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}'
</script>
</span> which has error of<span class="MathJax_Preview"><script type="math/tex">
\left|\left|\mathbf{x}-\mathbf{x}'\right|\right|_{1}\le\left(1+3\epsilon\right)\left|\left|\mathbf{x}_{tail\left(k\right)}\right|\right|_{1}
</script>
</span>.
</div>
<h1 class="Section">
<a class="toc" name="toc-Section-5">5</a> Precision Sampling<span class="FootOuter"><span class="SupFootMarker"> [A] </span><span class="HoverFoot"><span class="SupFootMarker"> [A] </span>Used in <i>Frequency Moments</i> chapter, for algorithms with <span class="MathJax_Preview"><script type="math/tex">
p>2
</script>
</span>.</span></span>
</h1>
<h3 class="Subsubsection-">
<a class="toc" name="toc-Subsubsection--11"></a>Problem Definition
</h3>
<div class="Unindented">
Given a stream <span class="MathJax_Preview"><script type="math/tex">
a_{1},..,a_{n}
</script>
</span> want to estimate <span class="MathJax_Preview"><script type="math/tex">
\sum_{i}a_{i}
</script>
</span> and reading only part of the stream. Sometimes the elements of the stream are bounded in given range, sometimes there is a continues penalty for reading each item and it is relative to the precision of that reading (precision model), then want also to minimize total penalty.
</div>
<h3 class="Subsubsection-">
<a class="toc" name="toc-Subsubsection--12"></a>Sub-sampling Model
</h3>
<div class="Unindented">
The data is in range <span class="MathJax_Preview"><script type="math/tex">
\left[0,1\right]
</script>
</span>, and penalty <span class="MathJax_Preview"><script type="math/tex">
1
</script>
</span> for reading each element (infinite precision), and penalty budget is <span class="MathJax_Preview"><script type="math/tex">
m
</script>
</span>. So sample <span class="MathJax_Preview"><script type="math/tex">
m
</script>
</span> i.i.d indices from <span class="MathJax_Preview"><script type="math/tex">
\left[n\right]
</script>
</span> with repetition called it <span class="MathJax_Preview"><script type="math/tex">
J
</script>
</span>, and output <span class="MathJax_Preview"><script type="math/tex">
S'=\frac{n}{m}\sum_{j\in J}a_{j}
</script>
</span>. We get <span class="MathJax_Preview"><script type="math/tex">
\mathbb{E}\left[S'\right]=S
</script>
</span> and <span class="MathJax_Preview"><script type="math/tex">
Var\left(S'\right)\le\left(\frac{n}{m}\right)^{2}m\left(1-0\right)=\frac{n^{2}}{m}
</script>
</span> by Chebyshev <span class="MathJax_Preview"><script type="math/tex">
\mathbf{P}\left[S'\in2\sigma\right]\ge3/4
</script>
</span>.
</div>
<h3 class="Subsubsection-">
<a class="toc" name="toc-Subsubsection--13"></a>Precision Model
</h3>
<div class="Unindented">
Can choose the accuracy of reading each <span class="MathJax_Preview"><script type="math/tex">
\tilde{a_{i}}
</script>
</span> in non-adaptive way. The precision is <span class="MathJax_Preview"><script type="math/tex">
\left|\tilde{a_{i}}-a_{i}\right|\le u_{i}
</script>
</span> and total penalty is <span class="MathJax_Preview"><script type="math/tex">
\frac{1}{n}\sum_{i}\frac{1}{u_{i}}
</script>
</span>. For single item, no information has penalty <span class="MathJax_Preview"><script type="math/tex">
0
</script>
</span> and good precision <span class="MathJax_Preview"><script type="math/tex">
u_{i}=\frac{1}{n}
</script>
</span> gives penalty <span class="MathJax_Preview"><script type="math/tex">
\approx1
</script>
</span>.
</div>
<h1 class="Section">
<a class="toc" name="toc-Section-6">6</a> <span class="MathJax_Preview"><script type="math/tex">
\ell_{p}
</script>
</span> Sampling
</h1>
<h3 class="Subsubsection-">
<a class="toc" name="toc-Subsubsection--14"></a>Problem Definition
</h3>
<div class="Unindented">
Given a frequency vector <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}\in\mathbb{R}^{n}
</script>
</span> want to sample random index from <span class="MathJax_Preview"><script type="math/tex">
\left[n\right]
</script>
</span>, where each <span class="MathJax_Preview"><script type="math/tex">
i
</script>
</span> has probability <span class="MathJax_Preview"><script type="math/tex">
\frac{\left|\mathbf{x}_{i}\right|^{p}}{\left|\left|\mathbf{x}\right|\right|_{p}^{p}}
</script>
</span>. Now the algorithm may return <span class="MathJax_Preview"><script type="math/tex">
Fail
</script>
</span> w.p. <span class="MathJax_Preview"><script type="math/tex">
\delta
</script>
</span>, and w.p. <span class="MathJax_Preview"><script type="math/tex">
1-\delta
</script>
</span> it is approximately correct (up to <span class="MathJax_Preview"><script type="math/tex">
\epsilon
</script>
</span>).
</div>
<h3 class="Subsubsection-">
<a class="toc" name="toc-Subsubsection--15"></a>Framework for <span class="MathJax_Preview"><script type="math/tex">
p=0
</script>
</span>:
</h3>
<div class="Unindented">
Define <span class="MathJax_Preview"><script type="math/tex">
supp\left(\mathbf{x}\right)=\left\{ i\in\left[n\right]:\:\mathbf{x}_{i}\ne0\right\} 
</script>
</span>, want sample coordinate uniformly at random among the non-zero coordinates. The steps in the framework are:
</div>
<ol>
<li>
<i>Sub-sample</i> coordinates of <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}
</script>
</span> with geometrically decreasing rate.
</li>
<li>
<i>Detect</i> if the resulting vector <span class="MathJax_Preview"><script type="math/tex">
\mathbf{y}
</script>
</span> is exactly <span class="MathJax_Preview"><script type="math/tex">
1
</script>
</span>-sparse (exactly one non-zero coordinate).
</li>
<li>
If it is, <i>Recover</i> the non-zero coordinate.
</li>

</ol>
<div class="Unindented">
<u>Algorithm:</u>
</div>
<ol>
<li>
Sub-sampling: choose (fully independent) random hash function <span class="MathJax_Preview"><script type="math/tex">
h:\left[n\right]\mapsto\left[\log n\right]
</script>
</span> s.t. <span class="MathJax_Preview"><script type="math/tex">
\forall i\in\left[n\right],l\in\left[\log n\right]:\:\mathbf{P}\left[h\left(i\right)=l\right]=2^{-l}
</script>
</span>. It does not add to 1, the remaining probability will be set <span class="MathJax_Preview"><script type="math/tex">
h\left(i\right)=null
</script>
</span>. For each <span class="MathJax_Preview"><script type="math/tex">
l\in\left[\log n\right]
</script>
</span> create a virtual stream <span class="MathJax_Preview"><script type="math/tex">
\mathbf{y}^{\left(l\right)}\in\mathbb{R}^{n}
</script>
</span> s.t. <span class="MathJax_Preview"><script type="math/tex">
\mathbf{y}_{i}^{\left(l\right)}=\mathbf{x}_{i}\cdot\mathbf{1}\left[i\in h^{-1}\left(l\right)\right]
</script>
</span>. In class we saw that if <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}\ne\mathbf{0}
</script>
</span> then <span class="MathJax_Preview"><script type="math/tex">
\exists l
</script>
</span> for which <span class="MathJax_Preview"><script type="math/tex">
\mathbf{y}^{\left(l\right)}
</script>
</span> is 1-sparse with constant probability (and indeed that non-zero coordinate was sampled w.p. <span class="MathJax_Preview"><script type="math/tex">
\left|supp\left(\mathbf{y}^{\left(l\right)}\right)\right|^{-1}
</script>
</span> by the fully independence). Repeat this step <span class="MathJax_Preview"><script type="math/tex">
\mathcal{O}\left(\log\frac{1}{\delta}\right)
</script>
</span> times.
</li>
<li>
Detection of 1-sparsity: Define <span class="MathJax_Preview"><script type="math/tex">
A:=\sum_{i}y_{i}
</script>
</span> and <span class="MathJax_Preview"><script type="math/tex">
B:=\sum_{i}y_{i}\cdot i
</script>
</span>. To detect if <span class="MathJax_Preview"><script type="math/tex">
\mathbf{y}=\mathbf{0}
</script>
</span> test if <span class="MathJax_Preview"><script type="math/tex">
A=0
</script>
</span>. To detect if <span class="MathJax_Preview"><script type="math/tex">
\left|supp\left(\mathbf{y}\right)\right|>1
</script>
</span>, create a vector <span class="MathJax_Preview"><script type="math/tex">
\tilde{\mathbf{y}}:=A\mathbf{e}_{B/A}
</script>
</span> that is, if <span class="MathJax_Preview"><script type="math/tex">
B/A
</script>
</span> is an integer, that <span class="MathJax_Preview"><script type="math/tex">
\tilde{\mathbf{y}}
</script>
</span> has <span class="MathJax_Preview"><script type="math/tex">
A
</script>
</span> at index <span class="MathJax_Preview"><script type="math/tex">
B/A
</script>
</span> and zeroes elsewhere. Then use Tug-of-War (AMS with <span class="MathJax_Preview"><script type="math/tex">
\epsilon_{AMS}:=0.5
</script>
</span>) to find if <span class="MathJax_Preview"><script type="math/tex">
\left|\left|\mathbf{y}-\tilde{\mathbf{y}}\right|\right|_{2}=0
</script>
</span> (i.e. input <span class="MathJax_Preview"><script type="math/tex">
\mathbf{y}
</script>
</span> is one sparse).
</li>
<li>
Recover the non-zero coordinate: report <span class="MathJax_Preview"><script type="math/tex">
B/A
</script>
</span>.
</li>

</ol>
<div class="Unindented">
The algorithm try to find an iteration of step 1 in which exists a &ldquo;level&rdquo; <span class="MathJax_Preview"><script type="math/tex">
l\in\left[\log n\right]
</script>
</span> s.t. <span class="MathJax_Preview"><script type="math/tex">
\mathbf{y}^{\left(l\right)}
</script>
</span> pass the other steps, if non such <span class="MathJax_Preview"><script type="math/tex">
\mathbf{y}
</script>
</span> found (over all iterations of step 1) - return <span class="MathJax_Preview"><script type="math/tex">
Fail
</script>
</span>. Note that total storage <span class="MathJax_Preview"><script type="math/tex">
\mathcal{O}\left(\log^{2}n\cdot\log\frac{1}{\delta}\right)
</script>
</span> <i>words</i> and probability for failure is <span class="MathJax_Preview"><script type="math/tex">
\delta
</script>
</span>, and <span class="MathJax_Preview"><script type="math/tex">
\epsilon:=1/n^{2}
</script>
</span>. Note also that the storage can be improved to be <i>bits</i> instead of words.
</div>
<h3 class="Subsubsection-">
<a class="toc" name="toc-Subsubsection--16"></a>Explaining the processing flow in a &ldquo;streaming&rdquo; way
</h3>
<div class="Unindented">
Assume we got from the stream an element <span class="MathJax_Preview"><script type="math/tex">
a_{i}\in\left[n\right]
</script>
</span> where <span class="MathJax_Preview"><script type="math/tex">
i
</script>
</span> is its index in the stream. Part (A) find the suitable level <span class="MathJax_Preview"><script type="math/tex">
l\in\left[\log n\right]
</script>
</span> using a hash function <span class="MathJax_Preview"><script type="math/tex">
l:=h\left(a_{i}\right)
</script>
</span> and then feed the &ldquo;virtual&rdquo; stream <span class="MathJax_Preview"><script type="math/tex">
l
</script>
</span> with <span class="MathJax_Preview"><script type="math/tex">
a_{i}
</script>
</span>. Consider Part (B) w.r.t. single &ldquo;virtual&rdquo; stream: given <span class="MathJax_Preview"><script type="math/tex">
a_{i}\in\left[n\right]
</script>
</span> it updates <span class="MathJax_Preview"><script type="math/tex">
B=B+a_{i}
</script>
</span> (as <span class="MathJax_Preview"><script type="math/tex">
B:=\sum_{i}y_{i}\cdot i=\sum_{i}\left(\mbox{\#times we sees the value \ensuremath{i\in\left[n\right]}}\right)\cdot i=\mbox{sum of the stream}
</script>
</span>) and <span class="MathJax_Preview"><script type="math/tex">
A=A+\begin{cases}
+1 & a>0\\
-1 & a<0
\end{cases}
</script>
</span> (the signs are to handle deletions, and <span class="MathJax_Preview"><script type="math/tex">
A:=\sum_{i}y_{i}=\sum_{i}\mbox{\#times we sees \ensuremath{i}}=\mbox{number of items in the stream after deletions}
</script>
</span>). Also, that part has 2 copies of AMS, the first gets <span class="MathJax_Preview"><script type="math/tex">
a_{i}
</script>
</span> as is, the other is being use only after the stream ends (i.e. &ldquo;offline&rdquo;) then it is being fed <span class="MathJax_Preview"><script type="math/tex">
B/A
</script>
</span> times the value <span class="MathJax_Preview"><script type="math/tex">
A
</script>
</span> (assuming <span class="MathJax_Preview"><script type="math/tex">
B/A
</script>
</span> is an integer, o.w. returns <span class="MathJax_Preview"><script type="math/tex">
Fail
</script>
</span>). The first AMS handle some compact sketch which will be used as a representation of <span class="MathJax_Preview"><script type="math/tex">
\mathbf{y}
</script>
</span>, the second has also compact sketch which represent <span class="MathJax_Preview"><script type="math/tex">
\tilde{\mathbf{y}}
</script>
</span>. Before each AMS estimate the <span class="MathJax_Preview"><script type="math/tex">
\ell_{2}
</script>
</span> norm, we subtract those sketches then estimate the norm for the <i>resulting sketch</i>. That is the estimation for <span class="MathJax_Preview"><script type="math/tex">
\left|\left|\tilde{\mathbf{y}}-\mathbf{y}\right|\right|_{2}^{2}
</script>
</span> that we wanted. If we got no failure until now (i.e. <span class="MathJax_Preview"><script type="math/tex">
A,B\ne0
</script>
</span> and <span class="MathJax_Preview"><script type="math/tex">
B/A\in\mathbb{N}
</script>
</span>), output <span class="MathJax_Preview"><script type="math/tex">
A
</script>
</span> and <span class="MathJax_Preview"><script type="math/tex">
B
</script>
</span>. 
</div>
<div class="Indented">
Note that we do not divide <span class="MathJax_Preview"><script type="math/tex">
B/A
</script>
</span> because then we can’t continue to perform more linear operations on the sampler (and then, for example, could not use it in AGM algorithm).
</div>
<h1 class="Section">
<a class="toc" name="toc-Section-7">7</a> Streaming on Graphs
</h1>
<div class="Unindented">
We will view undirected graph <span class="MathJax_Preview"><script type="math/tex">
G=\left(\left[n\right],E\right)
</script>
</span> with <span class="MathJax_Preview"><script type="math/tex">
\left|E\right|=m
</script>
</span>. Usually <span class="MathJax_Preview"><script type="math/tex">
n\le m
</script>
</span> and the stream is of edges in arbitrary order. We start by considering only edge insertions, and in Dynamic Graphs there are also edge deletion. For <u>most</u> of interesting problems we consider <b>semi-streaming</b> model, that is, storage <span class="MathJax_Preview"><script type="math/tex">
\tilde{\mathcal{O}}\left(n\right)
</script>
</span> (because it is impossible for less). 
</div>
<div class="Indented">
As for Dynamic Graphs model, assume that the operations are valid (deleting only edge that is now in the graph and etc). Moreover, only interested in fast <i>query-time</i> rather than update\construction time.
</div>
<h2 class="Subsection-">
<a class="toc" name="toc-Subsection--1"></a>Problems:
</h2>
<ul>
<li>
<b>Connectivity:</b> determine if the graph is connected, or if given <span class="MathJax_Preview"><script type="math/tex">
u,v
</script>
</span> are connected.
</li>
<li>
<b>Distances:</b> maintain all the distances in the graph for any pair <span class="MathJax_Preview"><script type="math/tex">
u,v
</script>
</span>.
</li>
<li>
<b>Triangle Counting: </b>report number of triangles <span class="MathJax_Preview"><script type="math/tex">
T
</script>
</span> in the graph <span class="MathJax_Preview"><script type="math/tex">
G
</script>
</span>.
</li>

</ul>
<h2 class="Subsection-">
<a class="toc" name="toc-Subsection--2"></a>Algorithms for Insertion Only Model
</h2>
<ul>
<li>
<b>Connectivity:</b> store a spanning tree in an incremental manner (less than <span class="MathJax_Preview"><script type="math/tex">
n
</script>
</span> edges) - storage <span class="MathJax_Preview"><script type="math/tex">
\mathcal{O}\left(n\right)
</script>
</span> words.
</li>
<li>
<b>Distances:</b> can be approximate within <span class="MathJax_Preview"><script type="math/tex">
2k-1
</script>
</span> for any integer <span class="MathJax_Preview"><script type="math/tex">
k\ge1
</script>
</span>, in storage <span class="MathJax_Preview"><script type="math/tex">
\mathcal{O}\left(n\right)
</script>
</span> words:\begin_inset Separator latexpar\end_inset<ul>
<li>
Use spanner: given edge <span class="MathJax_Preview"><script type="math/tex">
uv
</script>
</span> if spanner already contains a <span class="MathJax_Preview"><script type="math/tex">
2k-1
</script>
</span> path between <span class="MathJax_Preview"><script type="math/tex">
uv
</script>
</span> do nothing, else, add the edge to spanner.
</li>

</ul>

</li>

</ul>
<h2 class="Subsection-">
<a class="toc" name="toc-Subsection--3"></a>Algorithms for Dynamic Graphs
</h2>
<ul>
<li>
<b>Connectivity (AGM<a class="Label" name="Connectivity-(AGM):AGM"> </a>):</b> \begin_inset Separator latexpar\end_inset<ul>
<li>
Initialization: Define <span class="MathJax_Preview"><script type="math/tex">
N:={n \choose 2}
</script>
</span> and <span class="MathJax_Preview"><script type="math/tex">
\forall v\in V
</script>
</span> the vector <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}^{v}\in\mathbb{R}^{N}
</script>
</span> s.t. in any coordinate denoted as <span class="MathJax_Preview"><script type="math/tex">
\left\{ v,j\right\} 
</script>
</span>, and that pair in <span class="MathJax_Preview"><script type="math/tex">
E
</script>
</span> the value is <span class="MathJax_Preview"><script type="math/tex">
\begin{cases}
+1 & v<j\\
-1 & v>j
\end{cases}
</script>
</span> and o.w. <span class="MathJax_Preview"><script type="math/tex">
0
</script>
</span>.
</li>
<li>
Update: for each <span class="MathJax_Preview"><script type="math/tex">
v
</script>
</span> maintain <span class="MathJax_Preview"><script type="math/tex">
\ell_{0}
</script>
</span> sampler for <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}^{v}
</script>
</span> using the same coins. But repeat the sampler <span class="MathJax_Preview"><script type="math/tex">
\log n
</script>
</span> independent copies.
</li>
<li>
Output: start with partition <span class="MathJax_Preview"><script type="math/tex">
\Pi
</script>
</span> of <span class="MathJax_Preview"><script type="math/tex">
V
</script>
</span> into <span class="MathJax_Preview"><script type="math/tex">
n
</script>
</span> singletons. Repeat <span class="MathJax_Preview"><script type="math/tex">
\log n
</script>
</span> times using unique copy of <span class="MathJax_Preview"><script type="math/tex">
\ell_{0}
</script>
</span> sampler for each iteration:\begin_inset Separator latexpar\end_inset<ul>
<li>
For each connected component <span class="MathJax_Preview"><script type="math/tex">
Q\in\Pi
</script>
</span> (<span class="MathJax_Preview"><script type="math/tex">
Q\subseteq V
</script>
</span>) use <span class="MathJax_Preview"><script type="math/tex">
\ell_{0}
</script>
</span> sampler to pick an outgoing edge from that component. Formally, sample coordinate (i.e. edge) from the vector <span class="MathJax_Preview"><script type="math/tex">
\sum_{v\in Q}\mathbf{x}^{v}
</script>
</span>. Denoted all the resulting edges as <span class="MathJax_Preview"><script type="math/tex">
E'
</script>
</span>.
</li>
<li>
Merge any two connected components from <span class="MathJax_Preview"><script type="math/tex">
\Pi
</script>
</span> that are connected by some edge in <span class="MathJax_Preview"><script type="math/tex">
E'
</script>
</span>.
</li>

</ul>

</li>

</ul>

</li>

</ul>
<div class="Unindented">
Total storage is <span class="MathJax_Preview"><script type="math/tex">
\mathcal{O}\left(n\log^{4}n\right)
</script>
</span> bits: each of the <span class="MathJax_Preview"><script type="math/tex">
n
</script>
</span> samplers is <span class="MathJax_Preview"><script type="math/tex">
\mathcal{O}\left(\log^{3}n\right)
</script>
</span> bits, and there are <span class="MathJax_Preview"><script type="math/tex">
\log n
</script>
</span> iterations (which has to be &ldquo;fresh&rdquo; to prevent potential dependencies). Note that &ldquo;combining&rdquo; the <span class="MathJax_Preview"><script type="math/tex">
\ell_{0}
</script>
</span> samplers (as when estimating <span class="MathJax_Preview"><script type="math/tex">
\sum_{v\in Q}\mathbf{x}^{v}
</script>
</span>) are being done be summing the <span class="MathJax_Preview"><script type="math/tex">
A
</script>
</span>’s and <span class="MathJax_Preview"><script type="math/tex">
B
</script>
</span>’s outputs of each <span class="MathJax_Preview"><script type="math/tex">
\ell_{0}
</script>
</span> sampler.
</div>
<ul>
<li>
<b>Triangle Counting:</b> Let <span class="MathJax_Preview"><script type="math/tex">
N:={n \choose 3}
</script>
</span>, <span class="MathJax_Preview"><script type="math/tex">
n:=\left|V\right|,\:m:=\left|E\right|
</script>
</span> and assume given lower bound on number of triangles, that is given <span class="MathJax_Preview"><script type="math/tex">
0<t\le T
</script>
</span>.\begin_inset Separator latexpar\end_inset<ol>
<li>
First approach (additive error <span class="MathJax_Preview"><script type="math/tex">
\le\epsilon T
</script>
</span>)\begin_inset Separator latexpar\end_inset<ul>
<li>
Define <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}\in\mathbb{R}^{N}
</script>
</span> where any coordinate <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}_{S}
</script>
</span> correlate to a subset <span class="MathJax_Preview"><script type="math/tex">
S
</script>
</span> of 3 vertices, count number of edges internal to <span class="MathJax_Preview"><script type="math/tex">
S
</script>
</span>. <span class="MathJax_Preview"><script type="math/tex">
T
</script>
</span> is the number of coordinate with exactly <span class="MathJax_Preview"><script type="math/tex">
3
</script>
</span>. Use frequency moments to estimate <span class="MathJax_Preview"><script type="math/tex">
F_{p}:=\left|\left|\mathbf{x}\right|\right|_{p}^{p}
</script>
</span> for <span class="MathJax_Preview"><script type="math/tex">
p=0,1,2
</script>
</span> with approximation factor of <span class="MathJax_Preview"><script type="math/tex">
\gamma:=O\left(\frac{t}{\epsilon mn}\right)
</script>
</span>
</li>
<li>
Initially <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}=\mathbf{0}
</script>
</span>. Upon edge <span class="MathJax_Preview"><script type="math/tex">
uv
</script>
</span> increment any coordinate <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}_{S}
</script>
</span> s.t. <span class="MathJax_Preview"><script type="math/tex">
u,v\in S
</script>
</span>. Output <span class="MathJax_Preview"><script type="math/tex">
T:=F_{0}-1.5F_{1}+0.5F_{2}
</script>
</span>
</li>

</ul>

</li>
<li>
Second approach (additive error <span class="MathJax_Preview"><script type="math/tex">
\le\epsilon T
</script>
</span>)\begin_inset Separator latexpar\end_inset<ul>
<li>
Pick <span class="MathJax_Preview"><script type="math/tex">
k=O\left(\frac{TN}{\epsilon^{2}t^{2}}\right)=O\left(\frac{n^{3}}{\epsilon^{2}t}\right)
</script>
</span> random subsets <span class="MathJax_Preview"><script type="math/tex">
S_{1},..,S_{k}
</script>
</span> each of size <span class="MathJax_Preview"><script type="math/tex">
3
</script>
</span>.
</li>
<li>
Maintain each <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}_{S_{i}}
</script>
</span> explicitly.
</li>
<li>
Output: if <span class="MathJax_Preview"><script type="math/tex">
c
</script>
</span> is number of subsets with <span class="MathJax_Preview"><script type="math/tex">
S_{j}=3
</script>
</span> then return <span class="MathJax_Preview"><script type="math/tex">
\tilde{T}:=cN/k
</script>
</span>
</li>

</ul>

</li>
<li>
Can improve algorithm 2 by choosing <span class="MathJax_Preview"><script type="math/tex">
S_{j}
</script>
</span> more cleverly, from sets s.t. <span class="MathJax_Preview"><script type="math/tex">
\mathbf{x}_{S}\ge1
</script>
</span>, so the options are <span class="MathJax_Preview"><script type="math/tex">
N'\le nm\ll n^{3}
</script>
</span> (the estimator need to get a good estimation of <span class="MathJax_Preview"><script type="math/tex">
\left|\left|\mathbf{x}\right|\right|_{0}
</script>
</span> for that, and this algorithm wasn’t given in streaming model but can be convert to such model)
</li>

</ol>

</li>

</ul>
<h1 class="Section">
<a class="toc" name="toc-Section-8">8</a> Non-Streaming Sublinear Algorithms on Graphs 
</h1>
<div class="Unindented">
Problems:
</div>
<ul>
<li>
<b>Average Degree:</b> estimate the average degree in the graph.
</li>

</ul>

</div>
