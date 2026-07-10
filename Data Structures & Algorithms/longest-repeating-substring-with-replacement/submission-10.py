class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_counter = [0] * 26
        max_char_count = 0
        res = 0
        l = 0

        for r, c in enumerate(s):
            # 1. Inserisci il carattere corrente nella finestra
            character_counter[ord(c) - ord('A')] += 1
            
            # 2. Aggiorna il massimo nella finestra corrente
            max_char_count = max(max_char_count, character_counter[ord(c) - ord('A')])
            
            # 3. MENTRE la finestra non è valida, stringila da sinistra
            while (r - l + 1) - max_char_count > k:
                # Rimuovi il carattere a sinistra
                character_counter[ord(s[l]) - ord('A')] -= 1
                l += 1
                
                # CORREZIONE CRUCIALE: Ricalcola il vero max_char_count della finestra attuale
                max_char_count = max(character_counter)

            # 4. Ora siamo SICURI che la finestra è valida. Aggiorna il record
            res = max(res, r - l + 1)

        return res