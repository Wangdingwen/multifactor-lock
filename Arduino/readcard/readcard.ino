String comdata="";
#include <PN532.h>
#include <SPI.h>



/*Chip select pin can be connected to D10 or D9 which is hareware optional*/
/*if you the version of NFC Shield from SeeedStudio is v2.0.*/
#define PN532_CS 10

PN532 nfc(PN532_CS);
#define  NFC_DEMO_DEBUG 1

void setup(void) {
  pinMode(2,OUTPUT);
#ifdef NFC_DEMO_DEBUG
  Serial.begin(9600);
  Serial.println("Hello!");
#endif
  nfc.begin();

  uint32_t versiondata = nfc.getFirmwareVersion();
  if (! versiondata) {
#ifdef NFC_DEMO_DEBUG
    Serial.print("Didn't find PN53x board");
#endif
    while (1); // halt
  }
#ifdef NFC_DEMO_DEBUG
  // Got ok data, print it out!
  Serial.print("Found chip PN5"); 
  Serial.println((versiondata>>24) & 0xFF, HEX);
  Serial.print("Firmware ver. "); 
  Serial.print((versiondata>>16) & 0xFF, DEC);
  Serial.print('.'); 
  Serial.println((versiondata>>8) & 0xFF, DEC);
  Serial.print("Supports "); 
  Serial.println(versiondata & 0xFF, HEX);
#endif
  // configure board to read RFID tags and cards
  nfc.SAMConfig();
}

void loop(void) {
  uint32_t id;
  // look for MiFare type cards
  id = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A);

  if (id != 0) 
  {
#ifdef NFC_DEMO_DEBUG
    //Serial.print("Read card #"); 
    //Serial.println(id);
#endif
    uint8_t idkeys[]= { 0xFF,0xFF,0xFF,0xFF,0xFF,0xFF };
    if(nfc.authenticateBlock(1, id ,0x00,KEY_A,idkeys)) //authenticate block 0x00
    {
      //if authentication successful
      uint8_t idblock[16];
      //read memory block 0x00
      if(nfc.readMemoryBlock(1,0x00,idblock))
      {
#ifdef NFC_DEMO_DEBUG
        //if read operation is successful
        for(uint8_t i=0;i<16;i++)
        {
          //print memory block
          if (idblock[i] >= 15){
          Serial.print(idblock[i],HEX);
          }
          else{
            Serial.print("0");
            Serial.print(idblock[i],HEX);
          }
          
          //Serial.print(" ");
        }
        //Serial.println();
        Serial.println();
#endif
      }
    }


/*
comdata = "";




    uint8_t keys[]= { 0xFF,0xFF,0xFF,0xFF,0xFF,0xFF };
    if(nfc.authenticateBlock(1, id ,0x08,KEY_A,keys)) //authenticate block 0x08
    {
      //if authentication successful
      uint8_t block[16];
      //read memory block 0x08
      if(nfc.readMemoryBlock(1,0x08,block))
      {
#ifdef NFC_DEMO_DEBUG
        //if read operation is successful
        for(uint8_t i=0;i<16;i++)
        {
          //print memory block
          if (block[i] >= 15){
          Serial.print(block[i],HEX);
          }
          else{
            Serial.print("0");
            Serial.print(block[i],HEX);
          }
          
          //Serial.print(" ");
        }
        //Serial.println();
        Serial.println();
#endif

      }
    }
  */
  voice (1.5);
  }
comdata = "";

while(1){
    // look for MiFare type cards
  id = nfc.readPassiveTargetID(PN532_MIFARE_ISO14443A);
  if (id == 0) 
  {
    break;
  }
}
delay(1000);
}


void voice (double time)
{
    for(int i=0; i<250*time; i++)
    {
    digitalWrite(2,HIGH);
    delayMicroseconds(190);
    digitalWrite(2,LOW);
    delayMicroseconds(190);
    }
}
