#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

#include <openssl/rand.h>

#include "crypto.h"
#include "common.h"

#define LEDGER_FILE "ledger.bin"
#define PERMISSIONS (S_IRUSR | S_IWUSR)


int brute (char key_hash[]) {
  char alphabet[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  int i, j, k, l = 0;
  char test_key[] = "aaaa";
  char* hash;
  char* test_hash;
  for (i = 0; i < 62; i++) {
    for (j = 0; j < 62; j++) {
    for (k = 0; k < 62; k++) {
    for (l = 0; l < 62; l++) {
      test_key[0] = alphabet[i];
      test_key[1] = alphabet[j];
      test_key[2] = alphabet[k];
      test_key[3] = alphabet[l];

      test_hash = md5_hash(test_key, 4);
      memset(test_hash + 2, 0, 14);
      hash = md5_hash(test_hash, 2);

      if (memcmp(hash, key_hash, 16) == 0) {
        printf("KEY FOUND: %s\n", test_key);
        return 1;
      }
    }
    }
    }
  }

  printf("NO KEY FOUND :(\n");
  return -1;

}

int main(int argc, char **argv) {
  int fd;
  unsigned char key_hash[16];

  fd = open(LEDGER_FILE, O_RDONLY, PERMISSIONS);
  read(fd, key_hash, 16);
  close(fd);

  return brute(key_hash);

}
