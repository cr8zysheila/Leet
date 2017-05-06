max_score = 100
unsorted_scores = [37, 89, 89,  41, 65, 91, 91, 53]

def top_scores(scores, max_score):
	score_counts = [0] * (max_score + 1)
	sorted_scores = []

	for score in scores:
		score_counts[score] += 1

	for score, count in enumerate(score_counts):
		for i in range(0, count):
			sorted_scores.append(score)


	return sorted_scores



print top_scores(unsorted_scores, max_score)