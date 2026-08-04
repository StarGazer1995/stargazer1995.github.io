---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NCBI7IR%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T081600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQCGqPpCuB0SZISMVK6dJP%2BL4WAVDza2bVyJpeCExOrXHAIgPBffhfYtsJZSX7mnF68PiJ0wRaKf0MGFlnYxxRXDVt4q%2FwMIBxAAGgw2Mzc0MjMxODM4MDUiDGxfx2IE%2FHKdSn%2F2CSrcA%2FjcohWwEeuV1O7rgbKu1VYppXk1Gr6bFFPgQUAsWlF%2FuVpNOpyf1VWJRFklQClmFCELn3tR2EozHwXFFgW8FeAWPYGQD%2BV6KCYHE3f1gxCaRH7L4eDuAf4HkJ0uCqCsmL1B8zt0qMRVl02hkqNqHHEvp7VcENQdklG54F1wqa6EfY8tVWyj4b7eWzZv%2BRi5gci6cvoNkt1o4WLF7qHob7NYDbaKJloqOGRG2uJp0LM%2FCVgJ3BMI00okIDxyf%2Bo9KWp2Fut%2FcpYE17z4uH%2BCiTSmu90FevK7dEXLgPQuxVICRSA69Fh17nkal69tE%2FIHLmSrAM5jwdcqQ7CeMqmf4oomslqKeCKaIm2c70feUxC0zbOJe4%2FiDPyQfSZQcJIRE%2BBofPrc6Z0Sq7%2FSdZY2xO9uY6AvAxi0P8jS%2Fi0dlD3K%2BYIGPvWFO4kODN1AEWkBKflUMTixyiFqvCs%2BR6wHbtJ69TppRyZl8XIkT9xNRQArb%2Bwq7WFehqYU2Lh27aJROuNIzBoOLJ0hNVqf1lUB%2BMJ0BfUC0rC3o04fDSkp8eyGDhCMx4%2BNqVxXYCp4VcRrkOwxh9SAz%2Fq4hUXiPZQtuT20n7AnGU85iTOs%2BZWK29edJxqeWdwlv%2BKk2h41MOyExtMGOqUBFGeaLCbF0OMu1qPNwWJ8bTgWRPA38HjRTI3fAVG4SLA3t6OG8CZMwwkwrzWLMoEM8%2BIZ1St9TjJBpPZ1VEWkxQmROqBWmw5s%2B0QnNO%2FBp6hi5mydiY3LcX%2FyLPi9yQ2ya%2Bz73w%2B8XbtLr3KGaMKwVwwUkZncw2fsj3YNYhQvrcrFsaB34nqLzTR%2FaGjW4bL%2B7M1Emm8BkdaqoA73KmhtrHBtV%2BlQ&X-Amz-Signature=aa830cf976fddad0c73e492b85235d28310801b284464e8852d897bdb3ab2257&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
