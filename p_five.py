input_string=input()
rom_list=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX']
for i in range(0,len(rom_list)):
    if input_string==rom_list[i]:
        print(i+1)
