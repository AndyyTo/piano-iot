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
struct button{
  int pin;
  int frequency;
  String name;
};
const int pins_button[] = {4, 5, 6, 7, 8, 9, 10, 12};
const int frequencies[] = {NOTE_DO, NOTE_RE, NOTE_MI, NOTE_FA, NOTE_SO, NOTE_LA, NOTE_SI, NOTE_DO2};
const String names[] = {"Do", "Re", "Mi", "Fa", "Sol", "La", "Si", "Do2"};

const int buttonCount = 8;
const button buttons[buttonCount];

const int buzzerPin = 11;

void setup() {
  pinMode(buzzerPin, OUTPUT);

  for (int i = 0; i < buttonCount; i++) {
    buttons[i] = {pins_button[i], frequencies[i], names[i]};
    pinMode(buttons[i].pin, INPUT_PULLUP);
  }
  Serial.begin(9600);
}

void loop() {
  for (int i = 0; i < buttonCount; i++) {
    if (digitalRead(buttons[i].pin) == LOW) {
      Serial.println("button;" + buttons[i].name);
      playNote(buttons[i].frequency);
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

void playNote(int note) {
  tone(buzzerPin, note);
  Serial.println("frequency;" + String(note));
}