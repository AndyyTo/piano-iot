// Define note frequencies

#define NOTE_DO 262
#define NOTE_RE 294
#define NOTE_MI 330
#define NOTE_FA 349
#define NOTE_SO 392
#define NOTE_LA 440
#define NOTE_SI 493
#define NOTE_RE2 587
#define NOTE_G 415
#define NOTE_DO2 523
// Pin definitions for buttons
const int buttons[] = {4, 5, 6, 7, 8, 9, 10, 12};
const int buttonCount = 8;

const int buzzerPin = 11;

void setup() {
  pinMode(buzzerPin, OUTPUT);

  for (int i = 0; i < buttonCount; i++) {
    pinMode(buttons[i], INPUT_PULLUP);
  }
  Serial.begin(9600);
}

void loop() {
  for (int i = 0; i < buttonCount; i++) {
    if (digitalRead(buttons[i]) == LOW) {
      playNote(i + 1);
      delay(200);
      noTone(buzzerPin);
    }
  }

  if (Serial.available() > 0) {
    int command = Serial.parseInt();

    if (command >= 1 && command <= 8) {
      playNote(command);
      delay(200);
      noTone(buzzerPin);
      delay(300);
    }
  }
}

void playNote(int noteIndex) {
  switch (noteIndex) {
    case 1:
      tone(buzzerPin, NOTE_DO);
      Serial.println(String(NOTE_DO) + ";Do");
      break;
    case 2:
      tone(buzzerPin, NOTE_RE);
      Serial.println(String(NOTE_RE) + ";Re");
      break;
    case 3:
      tone(buzzerPin, NOTE_MI);
      Serial.println(String(NOTE_MI) + ";Mi");
      break;
    case 4:
      tone(buzzerPin, NOTE_FA);
      Serial.println(String(NOTE_FA) + ";Fa");
      break;
    case 5:
      tone(buzzerPin, NOTE_SO);
      Serial.println(String(NOTE_SO) + ";Sol");
      break;
    case 6:
      tone(buzzerPin, NOTE_LA);
      Serial.println(String(NOTE_LA) + ";La");
      break;
    case 7:
      tone(buzzerPin, NOTE_SI);
      Serial.println(String(NOTE_SI) + ";Si");
      break;
    case 8:
      tone(buzzerPin, NOTE_DO2);
      Serial.println(String(NOTE_DO2) + ";Do2");
      break;
  }
}