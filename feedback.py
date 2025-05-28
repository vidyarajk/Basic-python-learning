feedbck=["Great","Excellent","could be better","not satisfied"]
feedbck.append("Good")
positive_count=sum(1 for comment in feedbck if "great" in comment.lower() or "excellent" in comment.lower() or "good" in comment.lower())
print(f"No.of positive feedbacks: {positive_count}")
print("Every feedback:")
for x in feedbck:
    print(f"-{x}")