---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZMTOZXO%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T045345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJHMEUCIF2rUoLM8JDvrNgv%2FwplPXtystYfM1hWX%2B8QlOBMKz5pAiEAmq6KjAA%2BT7vnTki1OEZzZch9nlp1iEyCkLcwoduJ7Bwq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDFvkSpejiCyxcb93UyrcA%2B8MJXScFVjE%2FHe28Bq9%2BCvNw12SQ%2FOMibW%2Fj%2F0%2F8%2Bx3T2fPeMvJMbUYRgg1mceAbxKxW7Tx5HTgWGNOthnkB35Dm3xnzVvIcjH3Td5uA7KAt8AUqYsmLZMPzRXSnIwTu%2F%2BgGm4%2F41TkAzsguBCm3kDeonCc%2F%2FR05xB5OwjgAwqy2SyCpIEmp5i3xBfvKAfIQrL%2FoUWGaoTlXvTn8dYeOqoq4XoHw5al6SMdPGSY7UcjsNetslPrTepMd0S%2BhshscDu4tczU3%2FPp0%2Bf%2FSYFGDgXU8%2BHXEtVQ%2FngN1sSLbm9VlmzehgWS4TspDa3PirnViVbIsHa931K0h%2FIOt87arcp%2BbNXs%2BD%2FghwqsAsTa0jZ1B4VotCDVuj8gWJM3UpOmFQdwghhjAQmzkxYlIKPcG11rEzBZmmFKbGM79akLCWxnmHpG%2BmwSWkyKyOGtAD2Ixgk7sZ0kGLra1pxORnNYTnHfcP2I%2FSRpwDOjH%2BOT3inoYFQuVOrx%2FPlTYnMXYlaPHDN6HE%2FtLkOeeIwsvJ3VoL3y%2BNZjhgB%2FDVbwAZ8AOAJYjjurony8%2Ba3wsO%2B52U%2BnN4fB8kNm%2FL71j0A1aaouQo69tGGarCddxFolQSkTvwfWyiCo1tHTL8QbyC1aMNfuytMGOqUBzJDSreRGnYwyDHQs7qWpdSZ3dmImeih95857O1L%2FS7iKTwFUB0nSFYi3bmpP4HNPipuJXL3VhXLCtZTGTn7NMmKQnBZaAuIs6GM8UGmsA83ubBvi1w5WsDXdS7wOT5zxz2EYZ7VUW687dvP3tTDF%2BmgjaJnBqGLPLspxJpw31w8s0ZMpupdUrtZHtzufGWcJmfXehPsM%2F4VbCTDZA877DPbUPVMr&X-Amz-Signature=87e4d5f8ae81795289726ea454a6ad1b83b7c54fe83dccedf2ff0491ada1e99f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
