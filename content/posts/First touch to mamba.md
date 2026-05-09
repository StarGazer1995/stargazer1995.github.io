---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZX6WCSG%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T104606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQC%2BzOL5x4gEm%2BS9sTZc6QVlgEM18%2BSKZlk1Ty%2Fr6U9oZgIhAI2krf%2Fc0u6EWKkiqTCb65HZTfRUsZnnh2Ksm98aIcLEKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0lroDBwR9Ll0LTI4q3ANNFrM3l9RYUk9MKTuipBVRpmgyXOKTUUYR1dg%2Fd4ZacRfSFDLqZ1zQoJ865tuDkEQsQViewOToQMJkLBtTKYgRY0dhoxaJf78Y32I8XrVyDj8%2BOB8pWbAnqGN3GtdO6%2FlQ%2Fb9KTArP7IFHY2c2o7fNSkYvwsJO2xVEGjTJXKeYzEYJpgcsv%2F7mwb6X%2BgmZZCbY3u%2F%2FLABP%2FtGx0QA6g6zc8m5fDFfJL%2FlIgUG%2Fhxtto3nM7YVSWDIAR%2BcZh149AIzGEUEtWZlo%2BVzysSAf6UASpK35mgViO9FB2hmHwFYvjk2UQ%2FdeKuLRe2jc0m5H99zm2QQDu%2B8H6s%2B2SQzXD330fB%2BWj9DNfXJypoQ9nf3iEJTMrh6WT%2BTVK%2FFuM5zuiuPrruuhQHFPxN9JcZvwfv2Mo3Fb05Xv5%2BHPz9TYLRjIA8tVL5ucIkPUUVAM1PcQdw4Rd3wR%2FXJLQk54A4jw0A4bRynM0Aa3aH5HdaeNHv5DQ%2Bo2zrP4Sn50QzobNYy09Vf31qhJgJeFK%2BMOlGVnipXKnxLPyTtiMkFMCNNpBk8dQOcs0FSd25tgaW7DOciyPdd40djjuxvkFSMbAWkSvgSlPoBsYbjr0AKGkjnYLTdLzc39L%2B2ZdlPAo3LC%2BDC3%2BPvPBjqkAbIv5vvzbiBJkP6TaAiZ3Hs5sI2ZWFengo8SlTThtaNs0isB7CqxdEN%2FdlYJiAREyk%2BtzB18EEUcuYItQZgwtkBtkOfCTjS2zxZSOAckDybgJUtgVHuBaHbRd6dpFmSlPLXvS%2FGFghNVKdqXPnbCZzFXVp6Wm63k4oSY80Mj0BLTClCRbU1qA6rCeIiJR%2BBJqK2vSNvTC9H4rZRIc0EuzguuJ3iB&X-Amz-Signature=7c2b3ae024dfa3361f028d1dd2a69c1dbd576ad3aa508bdf4d601b7459ed9a1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

From the perceptive of the structure of mamba, this is a discrete selective space machine that runs in linear time using linear space.

lets say, matrix A is a state space matrix for the last system status h(t). we then can calculate the next h(t+1) based on the following equation:

$$
\begin{equation}h(t) = A*h(t-1) + B*x(t)\end{equation}
$$

$$
y = C*h(t)
$$

Where B is a weight for input x(t) and C is the weight for output y.

We define A matrix in a HiPPO matrix manner.

$$
A = \begin{cases} \sqrt{(2n+1)(2k+1)} && everything-below -diagonal \\
n+1 && on-diagonal \\
0 && everything-beyond-diagonal \end{cases}
$$

By doing this, we can use SVD partition for reducing the computing demand.

$$
A=V\Lambda V^* - PQ^T = V(\Lambda - (V^*P)(V^*Q)^*)V
$$

This can be done
