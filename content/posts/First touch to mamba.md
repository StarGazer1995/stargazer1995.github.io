---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7QFNDR7%2F20260612%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260612T212355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJHMEUCIQCAQkmprgzNWzU966CXCr%2F4buHre%2FIAME0551olWqYctwIgB8EQ%2FmLb7qVGxrp8NUJErzI1UoSEDbjMybzGFx2QuNQq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDOj%2BkJB6dinE4qzMFSrcA9x18jIGB8BoOsoI%2F1g%2BCLlldabTPlgYJxrR5toJVN83MpkfUBTn7QPgQSwBp4aZtY1zPdyXBe8PhIfLFUe%2FUCwHXcvGBninfXGocC9jvmLaNG%2BIAejctOeW4FAc%2BDOxYPcUh3wHEGRIamxJ0mdDsLR3mEZ%2BNk5NdZYf2CTG%2B7C77xg7jbEp4%2BfCZSrmlgilCGwoRRb%2B2FITcwv%2BMYkOu4hviEcw36auff6Q%2BKZL0DW54ehMI6kgqo1rOVif67oPznOv0GU9EMPqVcaiHpVtweocgQ2NIQGBloIgRVyG%2FDSD3BNnlUJ1cqs7z%2B71zU7Mqetyoap7FGdCIabPGEp73RCiqc9ZpB778VtPtfULGzwsy%2Bi%2FADWZHifTSJINRAe1Omon%2BcxrpwLIhAFTn2iRl4E%2FDx0WSp%2FUGRfBwTYDkQqoGTUQvrRGwJFSval7R0J34jyQ18M9XbICp031jm%2Bpyo%2BqqLvDhFokht4Y3CIiOJnwmQ5pp7LxXuSGfwljJrQLJASC%2BxzCSbg1tfHtxhRGBoR58xiOTGtTXFTGVqZp2utgMWMtC%2BgY%2FWmlqmHXLXx%2F4m3FhE0Bzoxb1cOV4hilWhTiWuV%2BSCxtbc40gtWYzmkqK%2B4FHH7N%2FXtOkWhKMJrJsdEGOqUBl50oojpGw1WNYbskI1XCFWL8WZh3Qkt60luRYrSR06ELnGQrA3KXKu4c%2ByS3SY4r8Ttf9jFwQ%2Bbo3QYj2YUpE%2Bi6irpW2ij8xwzTVhmn%2BNfd4Liw2s99sggBRO%2B2lgh2K8QVp4ahehrFVgGwUzZ72luPlOYJy49wSmv52ZHYkJS0NsQvdQAQvg4c6qwOCEcRoYwo87U8bo0RLDufjQS4C0JfRWrY&X-Amz-Signature=413d7acfb76c0e4c4a035b3415db6680024d001c4fc357a6476ba33fd502bc38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
