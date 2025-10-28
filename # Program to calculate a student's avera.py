# Program to calculate a student's average and determine approval status

def get_exam_scores():

      score_a = float(input("Enter the score for Exam A: "))
      score_b = float(input("Enter the score for Exam B: "))
      score_c = float(input("Enter the score for Exam C: "))
      return score_a, score_b, score_c
    
def calculate_average(scores):

  return sum(scores) / len(scores)

def display_result(average_score):

  passing_criteria = 7.0
  print(f"\nAverage Score: {average_score:.2f}") 

  if average_score >= passing_criteria:
    print("Student Status: Approved")
  else:
    print("Student Status: Not Approved")

if __name__ == "__main__":
  print("--- Student Average Score Calculator ---")
  
  exam_scores = get_exam_scores()

  average = calculate_average(exam_scores)

  display_result(average)