---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO73QMKI%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T191917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQCR7Cnbgnxi3W0TdYsk0dJJQgk%2FdJkbhk2Md%2FefmBpKpAIgbqjh3jrFivFf9Xp%2FbmGZWyi30MSpVW%2B0pJG5ogAIzZMq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDLDu9A26MT%2F8RmDUvCrcA9pDGA1KXXvdgQDb3EkgwCHr1nMCEK6kUufqD4H0j7Z5VIyGsE0xMrPK7ZlHz3mIAcEGUa052JDLNx7t1ogmgwWmkSQ%2FHJk1ROmyfTFnCPewBf%2BzKthIVBSo16Eo8WBH4PcOi%2FRe6smMrgRiB%2BGeNGU0ZEoQYQveCBsxCzdN42B05rftyz7X%2Ff5XaPd%2FVEJ5kW7sHgmmwwPT%2FBf6mo4hmVUf97I2TjWnI5%2BrvA8RxhMUYPo6F50pDOWQ6LUt%2Bv4BiRb6ILjpSrjRC8JwJgkc3rYN6D1mq87rWWecQS95RQPXw9r1NYFqz%2FtTJFT65rSDtoTy9N8tfU%2BKVnjZBysMndTvYTB173IPhli2%2FOysM89C18coYoPxdLmgZq1kWoB8ZW2iWslP9Rd7X9Yqiiz05lX8mEofSSakfY34YcZHDkW%2BJBdxHEYX%2BVqFWjz%2FZHCVKI0bWNVGPWvycurht0q9xp%2Bnz05v8lTQTiIvm%2Fua%2FJnkYTqeb4ZtBxDz68IuOtA7K8tT7xJqxQEMSB5kN0SSj4QtxPzyWv37feXCfk9Hd2biZyvDYvhrL0T1F7zOsNxrDw25KmUOnVgOPpTvzHXcLBFZKH6x5hvB7mAdsRrpOwdLRW%2FyMwkKk1rk4uVkMKSSyNMGOqUBj9UN0lNNz8RuisD3cUtx%2BQt2VOtphq3TaD5tmTcS1YJDfGCQVpLXUrOpFF%2BmRSCedL3T%2F2qSJG2UjFZ4c3%2Blz06ce9WZjDqI4ewwkqTACIzrJIGDUsRAmywuzS%2BXx5lMBkY8%2BYoFhA6k6aa%2FI6cWWIt1qryFffZQbhXBbhkrFmSsjUjk1yduyr2FPJsWCRVWsPnlmbfRGcQVIrDIMfuidRf4DkjS&X-Amz-Signature=6e4bdfbf4e2f1d4005a5cbbb3d784240e8fea15d30cde0eb1a376c1d6d415345&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
