import { View, Text, TouchableOpacity, StyleSheet } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { router } from "expo-router";

export default function JournalScreen() {
  return (
    <SafeAreaView style={styles.safe}>
      <View style={styles.header}>
        <Text style={styles.title}>My Journal</Text>
        <Text style={styles.streak}>Day 1 🌱</Text>
      </View>

      {/* Empty state */}
      <View style={styles.empty}>
        <Text style={styles.emptyIcon}>📓</Text>
        <Text style={styles.emptyTitle}>Your journal is empty</Text>
        <Text style={styles.emptyBody}>
          Start your first check-in. It only takes a couple of minutes.
        </Text>
        <TouchableOpacity style={styles.btn} onPress={() => router.push("/(tabs)/checkin")}>
          <Text style={styles.btnText}>Start check-in</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: "#fff" },
  header: { flexDirection: "row", justifyContent: "space-between", alignItems: "center", paddingHorizontal: 20, paddingVertical: 14, borderBottomWidth: 1, borderBottomColor: "#f4f4f5" },
  title: { fontSize: 17, fontWeight: "600", color: "#18181b" },
  streak: { fontSize: 13, color: "#a1a1aa" },
  empty: { flex: 1, alignItems: "center", justifyContent: "center", paddingHorizontal: 32, gap: 12 },
  emptyIcon: { fontSize: 52 },
  emptyTitle: { fontSize: 18, fontWeight: "600", color: "#18181b", textAlign: "center" },
  emptyBody: { fontSize: 14, color: "#71717a", textAlign: "center", lineHeight: 22 },
  btn: { marginTop: 8, backgroundColor: "#4f46e5", borderRadius: 16, paddingVertical: 14, paddingHorizontal: 32 },
  btnText: { color: "#fff", fontWeight: "600", fontSize: 15 },
});
