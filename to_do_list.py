t0_do_lst=["run","cook","study","teach"]
t0_do_lst.append("clean te house")
t0_do_lst.remove("cook")
if "teach" in t0_do_lst:
    print("dont forget to teach")
print("remaining to do list")
for task in t0_do_lst:
    print(f" ---{task}")