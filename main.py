import pymem
import pymem.process

dwEntityList = 0x4DD1E1C
dwGlowObjectManager = 0x531A118
m_iGlowIndex = 0x10488
m_iTeamNum = 0xF4


def main():

    print("Glow aktif edildi, İyi oyunlar.")

    oyun = pymem.Pymem("csgo.exe")

    sunucu = pymem.process.module_from_name(oyun.process_handle, "client.dll").lpBaseOfDll    

    while True:
        glow = oyun.read_int(sunucu + dwGlowObjectManager)
        for i in range(1, 32):  #Glow
            entity = oyun.read_int(sunucu + dwEntityList + i * 0x10)
            if entity:
                entity_team_id = oyun.read_int(entity + m_iTeamNum)
                entity_glow = oyun.read_int(entity + m_iGlowIndex)
                if entity_team_id == 2:  # Terörist
                    oyun.write_float(glow + entity_glow * 0x38 + 0x8, float(1))   # R
                    oyun.write_float(glow + entity_glow * 0x38 + 0xC, float(0))   # G
                    oyun.write_float(glow + entity_glow * 0x38 + 0x10, float(0))  # B
                    oyun.write_float(glow + entity_glow * 0x38 + 0x14, float(1))  # Opaklık
                    oyun.write_int(glow + entity_glow * 0x38 + 0x28, 1)           # Glow check
                elif entity_team_id == 3:  # CT
                    oyun.write_float(glow + entity_glow * 0x38 + 0x8, float(0))   # R
                    oyun.write_float(glow + entity_glow * 0x38 + 0xC, float(0))   # G
                    oyun.write_float(glow + entity_glow * 0x38 + 0x10, float(1))  # B
                    oyun.write_float(glow + entity_glow * 0x38 + 0x14, float(1))  # Opaklık
                    oyun.write_int(glow + entity_glow * 0x38 + 0x28, 1)           # Glow check

if __name__ == '__main__':
    main() #hook
