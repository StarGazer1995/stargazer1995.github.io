---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNGEFGGA%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T220939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIChbKRMTWWHNPK4ghD9Vuq8fg%2BTd5eox%2BnXWjybi%2FOn6AiEA6EgK8eNkDSUwiZOCFBnygMq6vhXanbMNM29ku6OqmpYq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDENV9CE4KAMfGOFU1CrcA9ys%2FuSjelg93JufzwVm5HWDrrrCh%2FvQrsFJ8q96zVNgmrdgHxHA%2BOiWCL57%2Bnlva5on%2FtkbocgIVtbMLPrXVL37IPUowToU3gTyei0qRC61XVr8cl%2BwN9rH4GCEpNN09iggt7qb1ZhLFO1iTMuvBt7XW3sZ84xlJD6pPTZrKs0cDMBvX70oIu0bVtPv0gcYplb3y2R41i8YkA3Kh5Sx7aq3IKcZ%2B2eEE8fCkTkA8c1vdtANOFsO03SXuB%2FHutGkRDBSxmL76gq5vZeTJHjFa3KvuMKuetV5siHcoulqYkRtKXkRRzQDm2QGe34zOsp9wnQpBXDjySl7TyGuymWDmmuO6OKuJZMvHxTJAOSWw2goAljD3pI1FkePjcx2iQtctUFUtq6lkXbGsR1PEA8%2BJytbvta1dUbgv0R2bPM575D0xvjn9surbTfAFzFamuEdm%2FgllY0uyDezTgd%2BQXA%2BOG06a%2BgEUT4VdvCwuJ8xHKJG4mxIU3bVkdLpCptecTvrSQ6ZFk8Wa1jmuZ2%2FWEGeKTGkMFScxas20lS6SAz4MhwNGf0PzM86PUGs0tvldSk6qa%2FkorlPczt2yZRmi1ijjI5rzuH2djH5LADEjd%2BHx%2F18sa9d26Y6eccDhbXdMO%2B2iNQGOqUBtG2rXPfVRNkhQzh%2Bw0FQ3D0fw2mNiSXYiD89gOLa6i4Usc7zdOVtj7OkyqhRVCWmERkc4abbX7h0o7DaToeRla2ucBgyjnCOn5TckzIEWQu4prjmWCtUvrXQKQwxEbcpnbGIpYmI1eWZGGTyMP09awz6cK8zypKP6BP%2BdIXzLxArswMzcV9P63LCuPXeOQbCU2gbajei7xdeI1tWPj5yXUuXFt5E&X-Amz-Signature=11aa68c86f50d877ef4d8387af39c2291edd17486356634904e8706944af83a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
