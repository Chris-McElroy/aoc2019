int main() {
  uint32_t input[] = {5, 9, 7, 3, 8, 5, 7, 1, 4, 8, 8, 2, 6, 5, 7, 1, 8, 0, 8, 9, 3, 5, 8, 9, 0, 4, 9, 6, 0, 1, 1, 4, 4, 5, 5, 2, 8, 0, 9, 7, 3, 5, 8, 5, 9, 2, 2, 6, 6, 4, 6, 0, 4, 2, 3, 1, 5, 7, 0, 7, 3, 3, 1, 5, 1, 9, 7, 8, 3, 3, 6, 3, 9, 1, 1, 2, 4, 2, 6, 5, 6, 6, 7, 9, 3, 7, 7, 8, 8, 5, 0, 6, 8, 7, 9, 0, 7, 3, 9, 4, 4, 9, 5, 8, 4, 1, 1, 2, 7, 0, 2, 4, 1, 5, 1, 0, 7, 9, 1, 2, 8, 4, 7, 5, 7, 7, 3, 4, 0, 3, 4, 7, 9, 0, 3, 1, 9, 1, 0, 0, 1, 8, 5, 3, 7, 5, 9, 1, 9, 3, 9, 4, 3, 2, 8, 2, 2, 2, 6, 4, 4, 8, 9, 7, 5, 7, 0, 5, 2, 7, 2, 1, 4, 4, 5, 1, 0, 4, 4, 7, 5, 7, 3, 1, 2, 2, 4, 2, 6, 0, 0, 5, 7, 4, 3, 5, 3, 5, 6, 8, 3, 4, 6, 2, 4, 5, 7, 6, 4, 3, 5, 3, 7, 6, 9, 2, 9, 3, 5, 3, 6, 6, 1, 6, 4, 6, 7, 7, 2, 9, 9, 2, 3, 6, 9, 3, 2, 0, 9, 3, 3, 6, 8, 7, 4, 6, 2, 3, 4, 2, 9, 2, 0, 6, 4, 1, 8, 3, 9, 5, 4, 9, 8, 1, 2, 9, 0, 9, 4, 1, 0, 5, 6, 1, 9, 1, 6, 9, 8, 8, 0, 1, 6, 6, 9, 5, 8, 9, 0, 2, 8, 5, 5, 4, 6, 1, 6, 2, 2, 6, 0, 0, 8, 4, 1, 0, 6, 2, 4, 6, 6, 0, 1, 7, 0, 3, 0, 8, 5, 9, 4, 7, 6, 3, 5, 2, 8, 2, 1, 9, 2, 1, 9, 1, 0, 2, 6, 5, 9, 9, 6, 4, 8, 7, 3, 2, 9, 0, 2, 0, 4, 6, 7, 6, 2, 1, 7, 1, 4, 8, 0, 8, 6, 6, 5, 7, 1, 1, 0, 5, 3, 9, 1, 6, 7, 0, 9, 6, 1, 9, 0, 4, 8, 5, 1, 0, 4, 2, 9, 6, 5, 5, 6, 8, 9, 4, 6, 1, 6, 0, 7, 4, 3, 8, 1, 7, 0, 7, 6, 7, 1, 0, 8, 6, 9, 4, 1, 1, 8, 4, 1, 9, 0, 1, 1, 3, 5, 0, 5, 4, 0, 4, 7, 6, 6, 2, 7, 2, 7, 2, 6, 1, 4, 6, 7, 6, 9, 1, 9, 5, 4, 2, 7, 2, 8, 2, 9, 9, 8, 6, 9, 2, 4, 7, 8, 1, 3, 7, 1, 3, 5, 8, 6, 6, 6, 5, 4, 6, 4, 8, 2, 3, 6, 2, 4, 3, 9, 3, 3, 4, 2, 0, 9, 8, 6, 7, 6, 1, 1, 6, 9, 1, 6, 4, 7, 5, 0, 5, 2, 9, 9, 5, 7, 4, 1, 2, 7, 7, 7, 0, 6, 7, 9, 4, 4, 7, 5, 6, 1, 9, 0, 3, 2, 8, 3, 3, 1, 4, 6, 4, 4, 1, 9, 9, 6, 3, 3, 8, 1, 9, 2, 7, 4, 4, 4, 4, 4, 4, 9, 1, 5, 3, 9, 6, 2, 6, 1, 2, 2, 7, 2, 5, 7, 1, 0, 9, 3, 9, 8, 9, 2, 2, 0, 0, 1, 5, 3, 4, 6, 4, 9, 3, 6, 2, 2, 5, 0, 0, 9, 5, 3, 1, 8, 3, 6, 0, 6, 9, 7, 4, 1, 1, 8, 9, 3, 9, 0, 6, 4, 2, 2, 7, 8, 7, 7, 4, 1, 1, 3, 7, 9, 7, 8, 8, 3, 2, 4, 0, 1, 0, 4, 6, 8, 7, 0, 3, 3, 6, 4, 5};
  uint32_t inputL[527150];
  // int start = 303673;

  for (int i=0; i < 527150; ++i) {
    inputL[i] = input[i%650];
  }
  int numRounds = 100;

  for (int r=0; r < numRounds; ++r) {
    int total = 0;
    for (int i=0; i < 527150; ++i) {
      total += inputL[i];
    }
    // std::cout << total%10;
    // std::cout << "\n";
    for (int i=0; i < 527150; ++i) {
      int prev = inputL[i];
      inputL[i] = total%10;
      total -= prev;
    }
  }

  for (int i=1007; i < 1007+8; ++i) {
    std::cout << int(inputL[i]);
  }
  return 0;
}
