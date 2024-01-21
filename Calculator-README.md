#Interest Calculator Code.
# Compound Interest Calculator

A Python script that calculates compound interest based on user-provided values for the principal amount, annual interest rate, and time.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Getting Started](#getting-started)
- [Command-line Options](#command-line-options)
- [Example](#example)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Python script serves as a compound interest calculator. It provides a simple and user-friendly command-line interface to calculate compound interest using the standard formula.

## Features

- **User-Friendly CLI:** Utilizes the Click library to create an intuitive command-line interface.
- **Accurate Calculation:** Calculates compound interest accurately based on the principal, annual interest rate, and time.

## Usage

### Prerequisites

- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`):
  - click

### Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/compound-interest-calculator.git
   cd compound-interest-calculator
#install dependencies 
pip install -r requirements.txt
#Run the script with the desired parameters:
python calculate_interest.py --principal 1000 --rate 5 --time 3
Replace the values with your specific inputs.

Command-line Options
--principal: Initial amount of money.
--rate: Annual interest rate (in %).
--time: Amount of years.

python calculate_interest.py --principal 1000 --rate 5 --time 3

#output
Principal: $1000
Annual Interest Rate: 5%
Time (years): 3
Interest Earned: $157.63
Total Amount: $1157.63
