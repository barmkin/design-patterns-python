from creational import Singleton

def main():
    s1 = Singleton()
    s2 = Singleton()

    s1.set_value('Design Patterns Singleton')

    print(f"s1 value: {s1.get_value()}")
    print(f"s2 value: {s2.get_value()}")

    print(f"Are s1 and s2 the same instance? {'Yes' if s1 is s2 else 'No'}")

if __name__ == "__main__":
    main()
