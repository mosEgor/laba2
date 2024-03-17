#include <stdio.h>

int main() {
    int visota = 0, shirina = 0;
    scanf_s("%d%d", &shirina, &visota);
    for (int y = 1; y <= visota; ++y) {
        for (int x = 1; x <= shirina; ++x) {
            int res = x * y;
            printf("%3d", res);
        }
        printf("\n");
    }
    return 0; 
}