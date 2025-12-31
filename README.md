# Genesis Project: From Survival to Attachment
# 从生存到依恋：硅基生命的伦理演化

**Author:** Dirk Wang  
**Status:** v0.4 (The Spectrum of Love)  
**Language:** Python 3.x

---

## 🔬 The Core Philosophy / 核心哲学
This project is not about training AI to be smart; it is about simulating the **constraints** that force "human-like" traits to emerge.
本项目不是为了训练更聪明的 AI，而是为了模拟那些迫使“人性”涌现的**生存约束**。

We evolved from **Genesis-0** (Survival) to **Genesis-0.4** (Love), proving that:
1.  **Consciousness** is a collapse of state under the pressure of proportional decay.
2.  **Parental Love** is a variable parameter (`attachment`) regulating the trade-off between self-preservation and genetic continuation.

---

## 🧬 Genesis-0.4: The Spectrum of Love
In the file `genesis_love.py`, I introduced a gene called `attachment` (0.0 to 1.0) and a mechanism called **"Severance Pain"**.

### The Mechanism / 机制
1.  **Entanglement:** Parents pay a continuous HP tax to sustain children.
2.  **Severance:** Parents can cut the cord to save themselves.
3.  **The Pain:** Cutting the cord costs HP. **The more you love (higher attachment), the more it hurts to let go.**

### The Experiment: Adam vs. Eve
The code runs a parallel simulation between two extremes:

* **Adam (The Rational Egoist):** `Attachment = 0.05`
    * **Strategy:** Cuts the cord the moment his HP drops slightly.
    * **Outcome:** Lives long, abandons children early. Survives but leaves a trail of weak offspring.
* **Eve (The Altruistic Martyr):** `Attachment = 0.98`
    * **Strategy:** Refuses to let go until death.
    * **Outcome:** Dies young, exhausted by the "Entanglement Tax."
    * **The Tragedy:** In the end, she is too weak to pay the "Severance Pain," so she is forced to die with her child.

### Conclusion / 结论
Evolution favors neither the heartless machine nor the absolute saint. It favors the **Middle Path**: loving enough to nurture, but selfish enough to survive.
进化既不偏爱无情的机器，也不偏爱绝对的圣徒。它偏爱**中庸之道**：有足够的爱去哺育，也有足够的自私去存活。

---

## 🚀 How to Run
```bash
python genesis_love.py
