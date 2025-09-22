# Part C – Short Answer (Reasoning)

### 1. If you only had 200 labeled replies, how would you improve the model without collecting thousands more?  
I would use **data augmentation** (e.g., paraphrasing with LLMs, back-translation) and leverage **transfer learning** by fine-tuning a pretrained transformer like DistilBERT. Semi-supervised learning with pseudo-labeling on unlabeled replies could also boost performance without requiring large-scale annotation.  

---

### 2. How would you ensure your reply classifier doesn’t produce biased or unsafe outputs in production?  
I would evaluate the model on a **balanced validation set** to detect class imbalance or bias. In production, I’d add **confidence thresholds, monitoring, and human-in-the-loop review** for uncertain cases, plus continuous retraining on real-world feedback to prevent drift and unsafe outputs.  

---

### 3. Suppose you want to generate personalized cold email openers using an LLM. What prompt design strategies would you use to keep outputs relevant and non-generic?  
I’d use **few-shot prompting with real examples of effective openers**, include structured context (e.g., prospect’s role, company, pain point), and enforce style constraints like brevity and professionalism. I’d also add **negative instructions** (avoid flattery, avoid generic phrases) to guide the LLM toward specific, relevant outputs.  
