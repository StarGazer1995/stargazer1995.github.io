---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644Y5HMME%2F20260906%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260906T214933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLXdlc3QtMiJHMEUCIQDjCacwqSPAtbv3e%2Bm9sh3xuI8jq8KnRUxzr0y38i4DvAIgcZV4tYNK9pbCunF8BZnQVQzOo2%2BuIhMRzUlsqANrOvAq%2FwMILhAAGgw2Mzc0MjMxODM4MDUiDD7fy5EQW1f%2BViIJpSrcA6b%2BDlFqf6%2BiXbhGZ3uS1tBdqqEZ7b7xTPsND74km%2FhbOKmRK6IOqupMR4HZgIiAzRGUYY6LyjR7dFerpaKSNefnNQq64LxE4zq2cLY%2Bcqcw88ncjgI94faRxq8UtOZ5OB1r7u0pz%2FsnPp26qBglqn8jEOTvIHm379y9NyVWlFHIsqJUZoJkdZJD4v%2BoPXK6fAV9gcemm596K2D7tXS%2B20FZVwxtXB868NjHpsYem2y56EyUNKGMzJ5V%2Bu6h3hre5FGxDsKDss2XOk7FJuU81qs6CmwUrkbr6pbueineoYFrWV2GrGPq8VAC3Nz5MlVg2bEl%2B7qCHNkuRMy6cTt7KWwsAbdcYbyL7M0tcxzwhtwWbUOqBkjCXizzgcASeAyCXaPuP2tf5Nvp3vjO919nk6obYoqGrWq3CskSe8iFpfmvB%2BjeQaAMeFUpSfoK4rrS1scPTF6aIwcMH3K3Zh1l%2BAvWgFsD2gWRgMGynwEVSpBVbjSerIgZWI2pb6wBI8WWYabAOBdRRRGieiI2sk%2BP77MfSaXIKcRPWeaGnLaiiQCCs9FGAT1EljNB1KZGh4MmqCin7DsV0ZFL%2B%2BiSFDtLdSxffsSZAd%2FSXo4QdOeme3cPEpU3jTWvw5fL4w5BMJ%2Bh99QGOqUBET9Qx4NnEXdUKTnxj6JqC3mDpb2yPfMhJCJlRnj9Jod8wy9deD4di3wCu0kqP2NPfxMGRmV56E5rAZ8jUO2e2jyrO9fIy9fVPjQOHmbwKGx0OtZS6a6JbWRGMOyCxKN46nhh2TGCswfrfeHiBendHedVz9y28AzM3UI4Tc1c35m2IBJeulsS%2FXFZZ8fYxcQLy4DBLQ3QScgQVvMhlEAgYDwhZe3e&X-Amz-Signature=51825e6cb994add03ae093a97d4c91a423db13e6738e91d6d7d2c81898079a48&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
