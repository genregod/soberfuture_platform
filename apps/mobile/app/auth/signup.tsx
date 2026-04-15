import { useState } from "react";
import { View, Text, TextInput, TouchableOpacity, StyleSheet, KeyboardAvoidingView, Platform } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { router } from "expo-router";

export default function SignupScreen() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  return (
    <SafeAreaView style={styles.safe}>
      <KeyboardAvoidingView behavior={Platform.OS === "ios" ? "padding" : "height"} style={styles.kav}>
        <View style={styles.inner}>
          <Text style={styles.brand}>SoberFuture</Text>
          <Text style={styles.sub}>Start your recovery journal</Text>

          <View style={styles.form}>
            <TextInput style={styles.input} placeholder="Your first name" placeholderTextColor="#a1a1aa" autoComplete="name" value={name} onChangeText={setName} />
            <TextInput style={styles.input} placeholder="Email" placeholderTextColor="#a1a1aa" keyboardType="email-address" autoCapitalize="none" autoComplete="email" value={email} onChangeText={setEmail} />
            <TextInput style={styles.input} placeholder="Password (8+ characters)" placeholderTextColor="#a1a1aa" secureTextEntry autoComplete="new-password" value={password} onChangeText={setPassword} />
            <TouchableOpacity style={styles.btn}>
              <Text style={styles.btnText}>Create journal</Text>
            </TouchableOpacity>
          </View>

          <Text style={styles.legal}>
            By signing up you agree to our Terms and Privacy Policy. Your journal is private and encrypted.
          </Text>

          <TouchableOpacity onPress={() => router.push("/auth/login")}>
            <Text style={styles.link}>Already have an account? <Text style={styles.linkBold}>Sign in</Text></Text>
          </TouchableOpacity>
        </View>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: "#fff" },
  kav: { flex: 1 },
  inner: { flex: 1, justifyContent: "center", paddingHorizontal: 24, gap: 8 },
  brand: { fontSize: 32, fontWeight: "700", color: "#4f46e5", textAlign: "center", marginBottom: 4 },
  sub: { fontSize: 14, color: "#71717a", textAlign: "center", marginBottom: 24 },
  form: { gap: 12 },
  input: { height: 52, borderWidth: 1.5, borderColor: "#e4e4e7", borderRadius: 16, paddingHorizontal: 16, fontSize: 15, color: "#18181b" },
  btn: { height: 52, backgroundColor: "#4f46e5", borderRadius: 16, alignItems: "center", justifyContent: "center", marginTop: 4 },
  btnText: { color: "#fff", fontWeight: "600", fontSize: 16 },
  legal: { fontSize: 11, color: "#a1a1aa", textAlign: "center", lineHeight: 16, marginTop: 12 },
  link: { textAlign: "center", fontSize: 14, color: "#71717a", marginTop: 8 },
  linkBold: { color: "#4f46e5", fontWeight: "600" },
});
