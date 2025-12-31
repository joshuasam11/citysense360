def planner_agent(task):
    return f"Plan created: break the task '{task}' into smaller steps and assign responsibilities."

def data_agent(task):
    return f"Data gathered: checked city records, reports and real-time feeds related to '{task}'."

def reporter_agent(task):
    return f"Report ready: recommended actions generated for '{task}' with priority levels."

def run_agents(task):
    step1 = planner_agent(task)
    step2 = data_agent(task)
    step3 = reporter_agent(task)

    return step1, step2, step3
