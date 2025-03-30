import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <View>{/*container-image*/}
        <Image source={{uri:"https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/2052px-Pok%C3%A9_Ball_icon.svg.png"}}
        width={200}
        height={200} 
        />
    </View>
      <View>{/*container-text*/}
        <Text style={styles.title}>Iniciar Sesion</Text>{/*title*/}
        <Text style={styles.label}>Correo </Text>{/*label*/}
        <TextInput style={styles.input}/>
        <Text style={styles.label}>Contraseña:</Text>{/*label*/}
        <TextInput style={styles.input}/>
        <Pressable style={styles.send}> {/*button*/}
          <Text style={styles.send.textButton}>Enviar</Text>
        </Pressable>
        <View>
          <View>{/*container-text*/}
            <Text style={styles.conatinerFooter}>¿Olvidaste tu contraseña?</Text>
            <Text style={styles.conatinerFooter}>Registrate</Text>
          </View>
        </View>
      </View>
    </View>
  );
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    padding: 10,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title:{
    fontSize: 30,
    fontWeight: 'bold',
  },
  label:{
    fontSize: 20,
    fontWeight: 'bold',
  },
  input:{
    borderRadius: 10,
    borderWidth: 2,
    borderColor: 'red',
    fontSize: 20,
    width:'auto',
    backgroundColor:'blue'
  },
  send:{
    backgroundColor: 'red',
    width: 'auto',
    haigth: 'auto',
    borderRadius: 10,
    marginTop: 15,
    alignItems: 'center',
    textButton:{
      color: 'black',
      fondWeight: 'bold',
      fondtSize: 30,
    }
  },
  conatinerFooter:{
    justifyContent: 'space-between',
    texts:{
      fontSize: 20,
      margin:5
    }
  }
});
