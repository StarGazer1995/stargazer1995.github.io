---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4E7EWZD%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T020102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDEdD3%2B0nlOP%2B9hxkhTm9JJX0HHD3d5DEtjfcqsxOcUXQIhAI7TZ8BsYrL4JRaj99jjIKdasA4yEcuErWFjWOjbeo4MKv8DCCsQABoMNjM3NDIzMTgzODA1Igx%2BArI7PEvokVNsOPoq3AMj3U5LWSbrWrbEvIsOl6YerDs37yDc%2B%2BPyxKDU%2B5u%2BbAmI5%2F69hrHO%2FPMyo0TX6ZOx0rfQxqE%2FFWruILgyF47Dgx1WOMNxSXmq8ubWEyql7YRGYi%2BKkAzBq3lKFC0DgiotQ0zJ3rrbW0kjKBhmgeorbXr5in5EO4fDhTfQjaK6l8eIBh%2BU4ofRNxjsLXRnlDWUVhzrmnoQdl4R9QSOKSxI6xOWxUdUMZNciWn3yVDlPZdBHSERt4a2qKNkfuBVTyHx5I5OTIQaPwSy1%2FB9qrktzxoxSF4bcuM89VewmiRWX444tcwx%2FZkMEa4JoQ6prQ07UJNiWdhi%2F2VNaugABSePzXnPjlVuhGpPQUItNlptnzOVUqAVqXBaGau7ZZIChxUDoWm124zXuvXL6VV5K3sPv4NroYHW6uhQDpEGzWLDeKsua2F1jjoOAJZHNc9yKDHNebiXklcBlwu39DzkqffKmMwyIwx5j9236bE2diqXptumuEmm2Es4UPvkhkY0ImFD4zJLsD2t7Sz9qUATf%2BeBipjDkDsd06TgRdnmOfAm0kilLz%2FNP33LPDU4aiwhIzOyWKiuLRifcdeKC6c8nWObBkmwzyHLXaj4LJg%2BYNhOJeKpk5Jw9mSf%2FQZDlzCf7%2BzRBjqkAbx7Zi%2Fjsc7BLnUQMhuqc0MWwqkm7AvE2gtAu08Shh7FnSoHh6pkJKhmPuBp84N%2F3gEnzL6sWm3mX3U%2FbGoAr%2FdeAiba%2BAm4zv13S26NUDKAbRVE0MrO%2BV636IWBwUUIPrV6WhOxWrB4aXgovXrvrVen0gc9CSLEaQKjb9eNKYjsMZsRFkZRhM0u2g6B%2FQ7Zq0QLKGsxhjaGJx4Gpp4Ihf1eBy9R&X-Amz-Signature=0671c839027c821d1d804485364e9c0c59913269d054eee3fb05c334da1bd07f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
