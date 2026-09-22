---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFELNQ6W%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T065845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDwKMVd1c8EW2fHfoxyu4D1kK69Y4CPmsluO8MWRNr6PAiAJj%2F2JKKSK7%2FkOOxwN2OvJPkwumQXx%2FS6j01N72wcBOSqIBAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuXQQjiTCNx%2B57eFiKtwDlOCV30unqdoemBcujUuXMLi4TpBNv8kNZ0UWGsXN7Q7PUgSUD1YzmN9NY5N6eXARESFOHl3Ietv9i6t4FKBTY%2BQXU6CipfCtlHKagp%2FWaEluXJMxIZjL6D2c0ZINz88JNOz94zXF5vVMIU2dnGpq%2FFQMrTVztV%2BOSzEK0rrvWnncb%2FlE6YcIaxNam%2B37i5euRMeSAIYoRzYvxkGOCzug2g9IYFYwL5g94ykAEGHEvMw%2BJBIwVAveIKhKF2cZC0MaduH9tc984VKPUqlSye41FfPckmYKZVu0xwuPDDnkmQjGUekn3aWlmnMNEmhFZRNP%2B3mAynkGM7%2FeLDNLXRPVS9oDnJ%2Bvxyd963ilKb%2FnqhkA%2FDJUrhOr81mYt3gvVRZOyvsweqzMuajSR44JYJHxSbexp5sn1CXlVbXZav%2FqBV1RdW%2BJj0tms3MGkRk4HR8zYBq44rTuCoYmGqyomLpCFdJjbxkysWC1eWO2GVp8Iw%2BliRZ0bNsYMjYWfrd1PpvmFmkaOuMZ%2BRn2gLCYLt54uAk2M1pQeIqlu465DUQwunU9A8xvyMBv8CH0JcQnqjuMs0aUptFeqr%2FHEZFDD1qwF4cCx%2BEsMyL5Pem2we60ro5Z0%2BBaR6%2FTqoMQ3AUwzsLI1QY6pgHu2RTdHs9uChEtIR7%2FVkQgTUpyJnMpsP1PengFV%2BptJG1FrT6CRkYP46EuvIh5o2kzL8%2Fvl%2FCNQpprRYAHdtWu73odNWvDyyeWNT4cJERBllu4jtE7zNKLRn80DmAGVwvwIbq28i00y7VIUHzHHKvhcg2nro8z7L3JAtdM9Ux04DFjKUAG%2BEHGBgHrmYhtwuqZ7Q888An8q22eg%2BcCEhjDNsbzloTt&X-Amz-Signature=fe6d91f217bdbcb862341d8a117d2210ed4897190b75b6f6bfb294a9e30e39b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
