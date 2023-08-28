import openai

jobname = "ftjob-CWmjNHgoAfrEyvjGev1P5Dgc"

r = openai.FineTuningJob.retrieve(jobname)
e = openai.FineTuningJob.list_events(id=jobname, limit=10)
print(f"status: {r}")
print("\n\n\n")
print(f"events: {e}")