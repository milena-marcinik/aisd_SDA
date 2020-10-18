from unittest import TestCase, main

from structures.queues import Stack


class TestStack(TestCase):
    def test_push(self):
        stack = Stack[int]()

        self.assertIsNone(stack.top)

    def test_push_init_elements(self):
        pass

    def test_front(self):
        stack = Stack[int]()
        stack.push(1)

        self.assertEqual(stack.front(), 1)

    def test_pop_stack_with_elements(self):
        stack = Stack[int]()
        stack.push(1)
        stack.push(2)
        stack.pop()

        self.assertEqual(stack.front(), 1)

    def test_pop_empty_stack(self):
        stack = Stack[int]()
        with self.assertRaises(Stack.EmptyStackError):
            stack.front()


if __name__ == '__main__':
    main()
