
# Promo Calculator

The Promo Calculator is a Python-based application designed to compute promotional pricing for a set of products based on predefined promotion rules. It processes a cart of items and applies applicable promotions to determine the total order value efficiently.

## Features

- **SKU Management**: Handles a list of single-character SKU IDs (e.g., A, B, C) with associated unit prices.
- **Promotion Types**:
  - **Quantity-Based Promotions**: Offers fixed pricing for purchasing a specific number of identical SKUs (e.g., 3 A's for 130).
  - **Combo Promotions**: Provides fixed pricing for purchasing a combination of different SKUs together (e.g., C + D = 30).
- **Total Calculation**: Computes the total order value after applying all relevant promotions.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ID-Mahone/promo-calculator.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd promo-calculator
   ```

3. **Install Dependencies**: *(If there are any; otherwise, skip this step)*

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Define Products and Promotions**: Specify the unit prices for each SKU and set up active promotions in the code.

2. **Create a Cart**: List the SKUs to be purchased.

3. **Calculate Total**: Run the program to compute the total order value after applying promotions.

For detailed examples and usage, refer to the provided test cases in the repository.

## Testing

The application includes unit tests to verify the correctness of the promotion calculations.

To run the tests:

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please fork the repository and create a new branch for any feature additions or bug fixes. Submit a pull request for review.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

David Manning
