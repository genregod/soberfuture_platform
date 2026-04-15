import { View, Text, StyleSheet } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

export default function ProfileScreen() {
  return (
    <SafeAreaView style={styles.safe}>
      <View style={styles.header}>
        <Text style={styles.title}>Profile</Text>
      </View>
      <View style={styles.empty}>
        <Text style={styles.icon}>👤</Text>
        <Text style={styles.msg}>Sign in to see your profile.</Text>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: "#fff" },
  header: { paddingHorizontal: 20, paddingVertical: 14, borderBottomWidth: 1, borderBottomColor: "#f4f4f5" },
  title: { fontSize: 17, fontWeight: "600", color: "#18181b" },
  empty: { flex: 1, alignItems: "center", justifyContent: "center", gap: 12 },
  icon: { fontSize: 48 },
  msg: { fontSize: 14, color: "#71717a" },
});
