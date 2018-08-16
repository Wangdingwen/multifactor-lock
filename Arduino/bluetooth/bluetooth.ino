String comdata="";

void setup()
{
  Serial.begin(9600);
}
 
void loop()
{
  while(Serial.available() > 0)
  {
    comdata += char(Serial.read());
    delay(2);
  }
  if (comdata.length() > 0)
  {
    if (comdata == "N7CU6235AJLJO7CVW6L73C6PURXQ545G"){
    Serial.print("SJ3M4GZVCZTAOME7APZRPQOCQJ5VNZY4");
    }
    comdata = "";
    }
  /*
  while(Serial.available() > 0)
  {
    comdata += char(Serial.read());
    delay(2);
  }
  if (comdata.length() > 0)
  {
    Serial.println(comdata);
    comdata = "";
  }*/
}
