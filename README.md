# PythonLab
Code and assignment for Python lab
Overview

This repository contains solutions for three problems that focus on creating reusable Python functions.
The objective is to write clean, modular logic that can be reused in multiple programs.

Problem (a): Virtual Deck of Playing Cards
Description

Create a reusable function that generates a virtual deck of 52 playing cards.

Card Representation

Card Values

Numeric cards from 2 to 9 are represented by their numbers

Special cards are represented as:

10 → T

Jack → J

Queen → Q

King → K

Ace → A

Suits

Hearts → h

Clubs → c

Diamonds → d

Spades → s

Card Format

Each card is stored as a two-character abbreviation:

First character → card value

Second character → suit

Examples: 2h, Kd, Qs, Ac

Requirements

The function should not take any parameters

Loops must be used to generate all cards

All cards should be stored in a list

The function should only return the list of cards

Problem (b): Split List into Chunks
Description

Given a list of elements and a number n, split the list into smaller sublists (chunks) where each sublist contains at most n elements.

This approach is useful for processing large data in smaller batches.

Example

Input list:

[1, 2, 3, 4, 5, 6, 7, 8]

Chunk size:

n = 3

Expected result:

[[1, 2, 3], [4, 5, 6], [7, 8]]

Requirements

Accept a list and a number n

Use loops to divide the list

Return a list containing all sublists

Problem (c): Pattern Matching in a String
Description

Given a string s and a pattern p, determine whether the pattern exists within the string.

If the pattern is found, return the starting index

If the pattern is not found, return -1

The comparison must be case-sensitive

Example

Input:

String: "Hello"

Pattern: "llo"

Output:

2

Explanation

The pattern "llo" begins at index 2 in the string "Hello".

Requirements

Accept two strings as input

Use loops for comparison

Return the index or -1 accordingly

Key Concepts Used

Reusable functions

Loops and iteration

Lists and strings

Modular programming

Beginner-friendly Python logic

Purpose

This project is designed for learning and academic purposes, focusing on understanding how to write reusable and well-structured Python functions.
