#include <Bounce2.h>

#define NOTE_DO 262
#define NOTE_RE 294
#define NOTE_MI 330
#define NOTE_FA 349
#define NOTE_SO 392
#define NOTE_LA 440
#define NOTE_SI 493
#define NOTE_DO2 523

struct button {
  int pin;
  int frequency;
  String name;
  Bounce debouncer;
};

const int pins_button[] = {4, 5, 6, 7, 8, 9, 10, 12};
const int frequencies[] = {NOTE_DO, NOTE_RE, NOTE_MI, NOTE_FA, NOTE_SO, NOTE_LA, NOTE_SI, NOTE_DO2};
const String names[] = {"Do", "Re", "Mi", "Fa", "Sol", "La", "Si", "Do2"};

float incomingFrequencies[16]; // Adjust the size as needed
int incomingIndex = 0;

const int buttonCount = 8;
button buttons[buttonCount];

const int buzzerPin = 11;

void setup() {
  pinMode(buzzerPin, OUTPUT);

  for (int i = 0; i < buttonCount; i++) {
    buttons[i] = {pins_button[i], frequencies[i], names[i], Bounce()};
    buttons[i].debouncer.attach(buttons[i].pin);
    buttons[i].debouncer.interval(10); // Set the debounce interval to 10 milliseconds
    pinMode(buttons[i].pin, INPUT_PULLUP);
  }
  Serial.begin(9600);
}

void loop() {
  for (int i = 0; i < buttonCount; i++) {
    buttons[i].debouncer.update();
    if (buttons[i].debouncer.fell()) {

      playNote(buttons[i]);
      delay(200);
      noTone(buzzerPin);
    }
  }

  if (Serial.available() > 0) {
    float frequency = Serial.parseFloat();


    if (frequency > 0) {
      incomingFrequencies[incomingIndex++] = frequency;
      if (incomingIndex >= 16) incomingIndex = 0; // Reset the index if it exceeds the array size

      playFrequency(frequency);
      delay(200);
      noTone(buzzerPin);
      delay(300);
    }
  }
}

void playNote(button button_) {
  tone(buzzerPin, button_.frequency);
  Serial.println(String(button_.frequency) + ";" + button_.name);
}

void playFrequency(float frequency) {
  tone(buzzerPin, frequency);
  Serial.println(String(frequency) + ";" +"");
}
