---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7R4AA75%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T203942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPSvfMEVbRjzvGMAt%2BW84CvfH5I6AhEkJbxaH4HaL18QIgUdee%2BAr66IXfrHej4vdH%2FcoZ2P2o04nZ9ACakNtGXjAqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBvAb9mCi2qaJRsrircA%2FNkUywVaZlKGICQmWXkBT3RIff1qQH7CqvfxQ2f9BC1e1sbzbxtWJXMfj76jrj1Ngo0XhrWREfZP8B4SN1cLLE4c%2FFgRSgYuwdZdks7xOEVjQGe9Nn1DUBYfNJxuYINfRQN3yrs%2FtG8x32IwkGG5oNpbmxq9%2Fm%2FeJpUZmMB8vYsBE8Gvwf14oiCVC4B55nAOQ1uO1cqK%2BhlVjjUbSqvQHtFx7wVrZq5bsCrlpaEAwcXvfwR2pH%2FxFh3BjcZ3h2OiYCGzA3cv0antQdzwxKrmPPJAJlGszU5lvy8oru4424LDvB%2Bh0bTha4miqcnMz397FaF39jF7f7h3%2BzDvmAzAIjAHOkYwbkuClzQ98Od63rznt3iFBCeONrrTnS3fiuDCLn8dZ%2BhAT0yOzRfU0Kb7njimA0U3JDiJvGddnNHGaXw4GKlxTydz1eqUENcaAiR3mSLT6LF2W8F9D5THPBpP1JEabXBJXXITEYURfuGJtr%2B%2B3g7wM372yLeTu%2BHdIq8YJxmssfPX6pLvL3WBqWTrFpHQRuPAoEB%2Fpqrh6dB1PdFTKloZC6X%2Bbl2w7oMBytWQ2O%2F%2BBPNd%2BD6lwyOFyGBiX9QxUMqphxuQ8uHsLlbj2o3iLdyloFSF3puXEl8MLGTqNAGOqUBHAdm%2B5OvxnV8BWevlt2DbvasjJpHgiPplNzl78FxIe%2B4Ju97a9%2BvZjQ1poRrGZzciySGatWSXMI8rIaOkGnoe%2BQ4EhpKdL4IFYKlwCW%2FZ%2FMDGdqYL6oIDq9ORLLO3hzTs3PzhX589xogmWnmN2oaFiVmsr%2BRKeANrlJPcHIlY0ZDiYOyhAGcSSWHSpEqB%2FicMFr7aSuRbtXRqhez%2F0OOsVSpvnGA&X-Amz-Signature=10ce108653ffb1b10b59e3bad49b42cf8a8fd64b84d1dbeaba07ea337845e026&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
