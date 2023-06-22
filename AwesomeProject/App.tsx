import React from 'react';
import axios from 'axios';
import AxisPad from 'react-native-axis-pad';
import type {PropsWithChildren} from 'react';
import { TouchableOpacity } from 'react-native';

import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  useColorScheme,
  View,
  Button
} from 'react-native';

import {
  Colors,
  DebugInstructions,
  Header,
  LearnMoreLinks,
  ReloadInstructions,
} from 'react-native/Libraries/NewAppScreen';

type SectionProps = PropsWithChildren<{
  title: string;
}>;

function Section({children, title}: SectionProps): JSX.Element {
  const isDarkMode = useColorScheme() === 'dark';
  return (
    <View style={styles.sectionContainer}>
      <Text
        style={[
          styles.sectionTitle,
          {
            color: isDarkMode ? Colors.white : Colors.black,
          },
        ]}>
        {title}
      </Text>
      <Text
        style={[
          styles.sectionDescription,
          {
            color: isDarkMode ? Colors.light : Colors.dark,
          },
        ]}>
        {children}
      </Text>
    </View>
  );
}

function processArm(){
  fetch('http://127.0.0.1:5000/arm', {
      method: 'POST',
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message: 'ArmDrone'
      }),
    })
      .then(response => response.json())
      .catch(error => {
        console.error(error);
      });
}

const processThrottle = async (throttleCommand) => {
  console.log(typeof(throttleCommand));
  await axios.post('http://127.0.0.1:5000/throttle', {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: throttleCommand,
    })
    // console.log("exited processThrottle")
      // .then(response => response.json())
      // .catch(error => {
      //   console.error(error);
      // });
}

const processRudder = async (rudderCommand) => {
  console.log(typeof(rudderCommand));
  await axios.post('http://127.0.0.1:5000/rudder', {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: rudderCommand,
    })
    // console.log("exited processThrottle")
      // .then(response => response.json())
      // .catch(error => {
      //   console.error(error);
      // });
}

const processElevation = async (pitchCommand) => {
  console.log(typeof(pitchCommand));
  await axios.post('http://127.0.0.1:5000/elevator', {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: pitchCommand,
    })
    // console.log("exited processThrottle")
      // .then(response => response.json())
      // .catch(error => {
      //   console.error(error);
      // });
}

const processAileron = async (aileronCommand) => {
  console.log(typeof(aileronCommand));
  await axios.post('http://127.0.0.1:5000/aileron', {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: aileronCommand,
  })
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.error(error);
    });
}

function App(): JSX.Element {
  const isDarkMode = useColorScheme() === 'dark';

  const backgroundStyle = {
    backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,
  };

  return (
    <SafeAreaView style={[styles.container, backgroundStyle]}>
      <TouchableOpacity style={styles.button} onPress={processArm}>
        <Text style={styles.buttonText}>Arm Drone</Text>
      </TouchableOpacity>
      <View style={styles.axisPadContainer}>
        <AxisPad
          resetOnRelease={true}
          autoCenter={true}
          onValue={({ x, y }) => {
            console.log(x, y);
            if (Math.abs(y) > Math.abs(x) && y < 0) {
              let throttleCommand = 'IncThrottle';
              processThrottle(throttleCommand);
            } else if (Math.abs(y) > Math.abs(x) && y > 0) {
              let throttleCommand = 'DecThrottle';
              processThrottle(throttleCommand);
            } else if (Math.abs(x) >= Math.abs(y)) {
              processRudder(x);
            }
          }}
        />
        <AxisPad
          resetOnRelease={true}
          autoCenter={true}
          onValue={({ x, y }) => {
            console.log(x, y);
            if (Math.abs(y) > Math.abs(x)) {
              processElevation(y);
            } else if (Math.abs(x) >= Math.abs(y)) {
              processAileron(x);
            }
          }}
        />
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  button: {
    backgroundColor: '#007AFF',
    padding: 10,
    borderRadius: 5,
    marginHorizontal: 20,
    marginVertical: 10,
    alignItems: 'center',
  },
  buttonText: {
    color: '#FFFFFF',
    fontSize: 18,
    fontWeight: 'bold',
  },
  axisPadContainer: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'center',
  },
});

export default App;
