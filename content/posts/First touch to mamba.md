---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OZ74RJQ%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T225721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGCh2M06q1xEhoq2sEIsQYfUKau7p4GHNju1chdBCfDaAiEAj8QLFiGRuszgx0aOWDDsTDF2pgYIQfDUeTAdbH3XC0Mq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDNBxrSKIrVHoXLS2WCrcA34B3z5XfKpDmNFMXE%2Fct36WVBbympUWBLXWlTHDx9AUpkCCJgInoXfbDLx60QerNp%2F9nJIWwX0TzrFHTA0c8YW%2BxlXNvPCT7SaSifEyAYpy2m92dSrrjjFiUIiWv%2Bz7li56dTaep1vr0DFc9QXtln%2BRhRI2R8mLm1InBEn3U%2FGSutJ8kZjoqpmAxN58ESwLVZlK%2Fo3FJEvvH89jBHzVKiwPHmPnsYTzS13IXsMOCxK0EbTVsyU9DYVUtf10Gq9I9X%2FDs1TMi%2BmW4B8SBuNlJq8XopYAz1st8OGUl0%2Beg1kr%2BwZIQrxxrGGAqtq3Gd5tnP%2FpXoCepyAIEYaZ9xi4D4GfO9VDYQ25QXS4iNWS6hHaA1qXCpQXNAZa0ssRcE6dJ%2Fq5wH1oXYP5N9yBGS88qSDEwny%2B1iqi5OMuFxBKQ8PWBlgAI4zFagqLRVB3Er4iMWPgkBI29oyQ06%2FpHLXeKUPkW8%2BnfR64Me99eV5LCzBENeS5OygcKDaxUrhgnmrFWvlIKxlRwILl78yHoVU6BVGC2oQ64Ot%2FprpeQ4eTAZXMoNtiqS0aPlnN%2F0qJvGoB4MVhxUZap%2B%2FYTfMY2mL%2B1phGUWPd0xCda9f%2Byibxs0BPIPZOJnP21yTPXgJmMOegjNEGOqUBMueG4vfmhhz6llgih3BmeW1vySkybftLLxzf2E5pTJxqsR41PG3SF6ofsDoJhxvg7TmJ6qkeZEQyCpLVxJB6FnXVAm0Z%2Fni4Xq7vei5rjva6psvxBFGrkXAbubFg0Wla6g%2BKZ31ITYLSbr4WdR6A9pqwT49AH6ItVU3hnNy51XjeEf6Im7YieMAz9Aom91Fy5U9vPrYnkyUq25vnglnx0TzncZ2R&X-Amz-Signature=656836f3c7ab9014bc68b9c4b1a223d1781da6aba08e361358616d09f694b6ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
