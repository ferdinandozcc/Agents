# Feedback Analyzer Agent

Clusters user feedback from multiple sources and surfaces the top themes, pain points, and positive signals.

## What it does

- Accepts raw feedback (NPS comments, support tickets, app reviews, survey responses)
- Clusters into 5-10 distinct themes
- Quantifies each theme by volume and sentiment
- Extracts representative quotes
- Recommends 3 actionable product improvements

## Usage

```bash
python product/feedback_analyzer/agent.py
```

Then either paste feedback directly or point to a file:
- *"Analyze the feedback in feedback.txt"*
- Paste raw text directly

## Output

- Executive summary
- Sentiment overview (positive / neutral / negative %)
- Theme table with quotes
- Top 3 pain points
- Top 3 positive signals
- Recommended actions
