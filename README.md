# Iranian National Code Validator
# Overview
This repository hosts a lightweight and efficient utility designed to algorithmically verify the validity of an Iranian National Code (Code Melli). While various external APIs exist for this purpose—often incurring per-call costs or introducing latency—this solution provides a concise, local alternative consisting of fewer than 20 lines of code. It is an ideal solution for developers requiring immediate, cost-effective validation without external dependencies.

# Key Features
Zero Dependencies: A standalone script that requires no external libraries.

Cost-Effective: Eliminates the need for paid API subscriptions for basic validation.

High Performance: Instantaneous execution with no network overhead.

# Usage
To utilize this script, simply execute the file within your environment. The function is designed to return a boolean value indicating the validity of the provided code.

Configuration:

The script currently utilizes a placeholder variable (denoted as a) containing a random 10-digit numeric string. To test specific scenarios, replace the value of variable a with a legitimate Iranian National Code.

Output: Returns True for a valid algorithm match and False otherwise.

# ⚠️ Important Limitation & Disclaimer
Please note: This utility validates the syntactic and algorithmic correctness of the National Code based on the standard check-digit algorithm.

False Positives: It is statistically possible to generate a random 10-digit number that satisfies the algorithm but does not belong to a real individual.

No Identity Verification: Unlike official government or banking APIs, this script does not query a central registry. It cannot confirm whether the National Code is currently assigned to a living citizen.

If your use case requires verifying the identity associated with a National Code or confirming its active status in the civil registry, we strongly recommend utilizing an official, connected API service.
