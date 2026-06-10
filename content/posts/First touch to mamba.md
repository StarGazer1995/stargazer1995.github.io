---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TCEL773%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T113802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIBW1CCNHZElhnJQtNGE%2BXmAql6mqQZTYhxciNnxvFfEIAiEAuG796GqBVblTRRXa7U3ywVRlsHvSej%2BDqyUxIVyPqpMqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMCV5P%2FmT29u1yTY7SrcA3gaHga532pfOaOpx71eRlIEq5HO2rVrSmPNo6w95PFI0Oi9txcas8WDlycfZBLDA511aDbvXD6bbAwOSznl8xGAq97Dt1GvNgEVJVaxiMqsSwrtdl75qg15pOJJy%2F44mm%2F9JZLSM2RMjFtTss4zZuIz%2Fc6hl%2B%2BHxs4T0Mk5Pb7wk9nQf9q%2BDAXcyTXz3nhefH%2BDPa4sizJWFAB7U%2F2bLpBwbxSHyeTRdquSXBCd72XlHAq8Jt7N4Bk86133TvMYe8MV%2Bg%2BErKjsRf2gADu8geSyODBJ%2FdP8tzioDuXVd1%2BFPdMBidFX66SaT3a%2FTKS%2FkCKGaNX0v7hKDTCK7gECMTkw%2FGDecHgOWIIEQmScsGdpfAxbusN6iK2VK%2FI%2FR8iMx6D62o4VxW00Ds7lSpR83Z9HdSX0DtxCRx3Ya4gehfyKFLkn3lpvPYo278k0%2FEFfN56cAOoc5U72NLQBgOBDhwz4MAbOWZ9fmz6OciEbfenqBidUlPqtTpibqTJZkLMKOroQloU1aw6VCYSG8crNwe5FDiRu3tB8BowQkxyPZrR8cyntO%2B%2BQpWPDuJ9fj17ka7BflCTSPaXHETuQjcwbjHaj%2BRkFagDIFg1kGCG2l8ZmYe0wYNnpAJg1nxgDMOKOpdEGOqUBxmjysAUjgw2ZB2b3m7ImKSht4Oo%2B3XljYDOSw448yGBXsFhsTycV%2BHn4uP%2Fthq6qHN8UipKolXZzZjY5lyfki41vNF%2FMGkVQrHcWaR20bkscRDF6h5hfvQ5LTw1Ze2B52%2FDcq925HK87extvU9OM47Z4piSdwXejh%2FJUpylTO9c4v0kZY6DCqJ3niZJI68sByjkfVOaDoP%2B07kqreQu5QcQFPlIH&X-Amz-Signature=0d9ae5a6620264cd6569b24a8d1513750dac260cdedce7db4462274bbbb837a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
