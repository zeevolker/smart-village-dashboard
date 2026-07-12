from scripts.generators.profile_generator import ProfileGenerator


def main():

    print("=== Age Engine Test ===\n")

    head = ProfileGenerator.generate_head_age()

    spouse = ProfileGenerator.generate_spouse_age(
        head_age=head,
    )

    children = ProfileGenerator.generate_children_ages(
        count=4,
        head_age=head,
    )

    parent = ProfileGenerator.generate_parent_age(
        head_age=head,
    )

    sibling = ProfileGenerator.generate_sibling_age(
        head_age=head,
    )

    print("Head     :", head)
    print("Spouse   :", spouse)
    print("Children :", children)
    print("Parent   :", parent)
    print("Sibling  :", sibling)

    assert parent > head
    assert spouse >= 18

    if children:
        assert children == sorted(children, reverse=True)

    print("\n✅ All tests passed.")


if __name__ == "__main__":
    main()