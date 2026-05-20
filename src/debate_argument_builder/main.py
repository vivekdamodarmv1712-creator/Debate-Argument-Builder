import sys
import warnings
from datetime import datetime

from debate_argument_builder.crew import DebateArgumentBuilder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the Debate Argument Builder crew.
    """

    print("\n🎯 Enter Debate Topic:")
    topic = input("> ")

    print("\n⚖️ Choose Side (for / against):")
    side = input("> ").strip().lower()

    if side not in ["for", "against"]:
        raise ValueError("Side must be either 'for' or 'against'")

    inputs = {
        "topic": topic,
        "side": side,
        "current_year": str(datetime.now().year)
    }

    result = DebateArgumentBuilder().crew().kickoff(inputs=inputs)

    # Task outputs (sequential order)
    arguments = result.tasks_output[0].raw
    counterarguments = result.tasks_output[1].raw
    rebuttals = result.tasks_output[2].raw

    print("\n" + "=" * 60)
    print("🧠 ARGUMENTS")
    print("=" * 60)
    print(arguments)

    print("\n" + "=" * 60)
    print("⚔️ COUNTERARGUMENTS")
    print("=" * 60)
    print(counterarguments)

    print("\n" + "=" * 60)
    print("🔁 REBUTTALS")
    print("=" * 60)
    print(rebuttals)

    print("\n📄 Final output saved to: output/debate_brief.md")


def train():
    """
    Train the crew.
    """
    inputs = {
        "topic": "AI regulation",
        "side": "for",
        "current_year": str(datetime.now().year)
    }

    try:
        DebateArgumentBuilder().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"Error during training: {e}")


def replay():
    """
    Replay a specific task execution.
    """
    try:
        DebateArgumentBuilder().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"Error during replay: {e}")


def test():
    """
    Test the crew execution.
    """
    inputs = {
        "topic": "AI regulation",
        "side": "against",
        "current_year": str(datetime.now().year)
    }

    try:
        DebateArgumentBuilder().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"Error during testing: {e}")


if __name__ == "__main__":
    run()